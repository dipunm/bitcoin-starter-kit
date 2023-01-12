function (copy_dir TARGET SRC)
    file(GLOB_RECURSE SRC_FILES ${SRC}/*)

    foreach(SRC_FILE ${SRC_FILES})
        get_filename_component(FILE_NAME ${SRC_FILE} NAME)
        set(DST_FILE ${CMAKE_CURRENT_BINARY_DIR}/../modules/${FILE_NAME})
        add_custom_command(
            OUTPUT ${DST_FILE}
            COMMAND ${CMAKE_COMMAND} -E copy ${SRC_FILE} ${DST_FILE}
            DEPENDS ${SRC_FILE}
        )
        target_sources(${TARGET} INTERFACE ${DST_FILE})
    endforeach()
endfunction()

copy_dir(usermod_badger2040 ${GITHUB_WORKSPACE}/project/src)