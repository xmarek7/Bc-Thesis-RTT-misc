#include "psample_calculator.h"


/*
 * Calculates maximal possible psamples value for given test and file length
 *
 * @test_id - wanted test id
 * @ntuples - parameter of test - ignored in case of test not requiring this setting
 * @file_length - bytes length of file set for test
 * @return - maximal possible number of pvalues
 */
// TODO ? - similar map as for bytes_per_psample, but for max/min_psample for test
// support for this can be easily implemented later.
long long calculate_psamples(int test_id, int ntuples, long long file_len){
    long long bytes = get_bytes_per_psample(test_id, ntuples);
    if (bytes == -1) {
        return -1;
    }
    if (test_id == 0){
        return (file_len - 24) / bytes;
    }
    return file_len / bytes;
}


/*
 * Functions as a map - assigns a number of bytes per p-value to a test and ntuples setting
 * Works only for tests marked as 'good' by Dieharder creators.
 *
 * @test_id - wanted test id
 * @ntuples - parameter of test - ignored in case of test not requiring this setting
 * @return - number of bytes consumed per psample, -1 in case of invalid test or ntuples for given test
 */
long long get_bytes_per_psample(int test_id, int ntuples){
    switch (test_id) {
        case 0:
            return 153600;
        case 1:
            return 4000020;
        case 2:
            return 5120000;
        case 3:
            return 2400000;
        case 4:
            return 1048584;
        case 8:
            return 256004;
        case 9:
            return 5120000;
        case 10:
            return 96000;
        case 11:
            return 64000;
        case 12:
            return 48000;
        case 13:
            // TODO - One of irregular tests
            return -1;
        case 15:
            return 400000;
        case 16:
            //TODO - One of irregular test
            return -1;
        case 17:
            return 80000000;
        case 100:
            return 400000;
        case 101:
            return 400000;
        case 102:
            return 400000;
        case 200:
            // TODO - what about bigger ntuples?
            if (ntuples < 1 || ntuples > 12){
                return -1;
            }
            // Those 4 bytes at the end are really there
            return ntuples * 800000 + 4;
        case 201:
            // TODO - what about bigger ntuples?
            if (ntuples < 2 || ntuples > 5){
                return -1;
            }
            return ntuples * 40000;
        case 202:
            // TODO - what about bigger ntuples?
            if (ntuples < 2 || ntuples > 5){
                return - 1;
            }
            return ntuples * 400000;
        case 203:
            // TODO - what about bigger ntuples?
            if (ntuples < 0 || ntuples >32){
                return -1;
            }
            return (ntuples + 1) * 4000000;
        case 204:
            return 40000;
        case 205:
            return 614400000;
        case 206:
            return 51200000;
        case 207:
            // TODO - One of irregular tests
            return -1;
        case 208:
            // TODO - One of irregular tests
            return -1;
        case 209:
            return 260000000;
        default:
            return -1;
    }
}
























