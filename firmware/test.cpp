int test() {
#if not defined HAVE_CONFIG_H
#  error "Set ECMULT_GEN_PREC_BITS to 2, 4 or 8."
#endif
    return 0;
}