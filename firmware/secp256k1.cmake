# Create an INTERFACE library for our C module.
add_library(secp256k1 INTERFACE)

# Add our source files to the lib
target_sources(secp256k1 INTERFACE
    # ${SECP256K1_PATH}/secp256k1/src/secp256k1.c
    # ${SECP256K1_PATH}/mpy/config/ext_callbacks.c
    # ${SECP256K1_PATH}/mpy/libsecp256k1.c
    ${CMAKE_CURRENT_LIST_DIR}/test.cpp
)

# Add the current directory as an include directory.
target_include_directories(secp256k1 INTERFACE
    ${SECP256K1_PATH}/secp256k1
    ${SECP256K1_PATH}/secp256k1/src
    ${SECP256K1_PATH}/mpy/config
)
target_compile_options(secp256k1 INTERFACE
    -DHAVE_CONFIG_H
    -DMODULE_SECP256K1_ENABLED=1
    -Wno-unused-function
    -Wno-error
    -DDIPUN
)


# Link our INTERFACE library to the usermod target.
target_link_libraries(usermod INTERFACE secp256k1)
