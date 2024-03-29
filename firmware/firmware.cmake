# include(${FIRMWARE_DIR}/secp256k1.cmake)
include(${FIRMWARE_DIR}/ubitcoin.cmake)
include(${PIMORONI_PICO_PATH}/micropython/modules/badger2040-micropython.cmake)

function (copy_dir TARGET SRC)
    file(GLOB_RECURSE SRC_FILES ${SRC}/*)
    set(DST_FILES "")
    foreach(SRC_FILE ${SRC_FILES})
        get_filename_component(FILE_NAME ${SRC_FILE} NAME)
        set(DST_FILE ${CMAKE_CURRENT_BINARY_DIR}/../modules/${FILE_NAME})
        list(APPEND DST_FILES ${DST_FILE})
    endforeach()
    add_custom_command(
        OUTPUT ${DST_FILES}
        COMMAND ${CMAKE_COMMAND} -E make_directory ${CMAKE_CURRENT_BINARY_DIR}/../modules/
        COMMAND ${CMAKE_COMMAND} -E copy_directory ${SRC} ${CMAKE_CURRENT_BINARY_DIR}/../modules/
        VERBATIM
    )
    target_sources(${TARGET} INTERFACE ${DST_FILES})
endfunction()

copy_dir(usermod_badger2040 ${FIRMWARE_DIR}/src)