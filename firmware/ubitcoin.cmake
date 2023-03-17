# Create an INTERFACE library for our C module.
add_library(ubitcoin INTERFACE)

# Add our source files to the lib
target_sources(ubitcoin INTERFACE
    ${UBITCOIN_PATH}/src/HDWallet.cpp
)

# Add the current directory as an include directory.
target_include_directories(ubitcoin INTERFACE
    ${UBITCOIN_PATH}/src
)

# Link our INTERFACE library to the usermod target.
target_link_libraries(usermod INTERFACE ubitcoin)
