#include "Bitcoin.h"

extern "C" {

#include <uBitcoinWrapper.h>

mp_obj_t ubitcoin_fingerprint(void) {

    HDPrivateKey hd(
        reinterpret_cast<const uint8_t*>("add good charge eagle walk culture book inherit fan nature seek repair"), 
        reinterpret_cast<const uint8_t*>("")
    );

    uint8_t fingerprintArray[4];
    hd.fingerprint(fingerprintArray);
    const char *message = reinterpret_cast<char*>(fingerprintArray);
    // const char *message = "Hello from uBitcoin!";
    return mp_obj_new_str(message, strlen(message));
}

}