#!/bin/bash

pushd firmware/tmp/secp256k1-embedded
git diff > ../../secp256k1_embedded.patch
pushd secp256k1
git diff > ../../../secp256k1.patch
popd
popd
