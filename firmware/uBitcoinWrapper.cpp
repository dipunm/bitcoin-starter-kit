#include "Bitcoin.h"

external "C" {

#include <uBitcoinWrapper.h>

mp_obj_t ubitcoin_fingerprint(void) {

    HDPrivateKey hd("add good charge eagle walk culture book inherit fan nature seek repair", "");
    const char *message = hd.fingerprint()
    // const char *message = "Hello from uBitcoin!";
    return mp_obj_new_str(message, strlen(message));
}

}