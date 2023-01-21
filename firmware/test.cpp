int test() {
#if not defined DIPUN
#  error "PARAM DIPUN NOT DEFINED!"
#endif
    return 0;
}