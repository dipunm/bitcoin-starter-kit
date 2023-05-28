#include <uBitcoinWrapper.h>

STATIC MP_DEFINE_CONST_FUN_OBJ_0(ubitcoin_fingerprint_obj, ubitcoin_fingerprint);

STATIC const mp_rom_map_elem_t ubitcoin_module_globals_table[] = {
    { MP_ROM_QSTR(MP_QSTR_fingerprint), MP_ROM_PTR(&ubitcoin_fingerprint_obj) }
};

STATIC MP_DEFINE_CONST_DICT(ubitcoin_module_globals, ubitcoin_module_globals_table);

const mp_obj_module_t ubitcoin_module = {
    .base = { &mp_type_module },
    .globals = (mp_obj_dict_t*)&ubitcoin_module_globals,
};

MP_REGISTER_MODULE(MP_QSTR_ubitcoin_module, ubitcoin_module);
