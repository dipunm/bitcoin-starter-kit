# Create an INTERFACE library for our C module.
add_library(ubitcoin INTERFACE)

# Add our source files to the lib
target_sources(ubitcoin INTERFACE
    ${CMAKE_CURRENT_SOURCE_DIR}/uBitcoinWrapper.c
    ${CMAKE_CURRENT_SOURCE_DIR}/uBitcoinWrapper.cpp
    ${UBITCOIN_PATH}/src/HDWallet.cpp
    ${UBITCOIN_PATH}/src/Micropy.c
)

# Add the current directory as an include directory.
target_include_directories(ubitcoin INTERFACE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${UBITCOIN_PATH}/src
)

target_compile_options(ubitcoin INTERFACE
    -DUSE_STDONLY
    -DUSE_STD_STRING=0
)

list(APPEND MICROPY_CPP_FLAGS_EXTRA 
    -DUSE_STDONLY
    -DUSE_STD_STRING=0
)

# Link our INTERFACE library to the usermod target.
target_link_libraries(usermod INTERFACE ubitcoin)