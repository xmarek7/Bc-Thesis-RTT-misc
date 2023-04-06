//
// Created by Tomáš on 24.03.2023.
//

#include "main.h"
#include "psample_calculator.h"
#include "stdio.h"

#define DATASIZE_400MB 419430400
#define TESTS_COUNT 27

int main(){
    int test_ids[] = {0, 1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 15, 16, 17, 100, 101, 102, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209};
    test_file(test_ids, DATASIZE_400MB);
}

void test_file(int *test_ids, long long file_size){
    for (int i = 0; i < TESTS_COUNT; i++) {
        int test_id = test_ids[i];
        printf("Result for test with id %d\n", test_id);
        if (test_id == 200) {
            for (int ntup = 1; ntup <= 12; ntup++){
                int psamples = calculate_psamples(test_id, ntup, file_size);
                printf("    ntuples = %d, suggested psamples are %d\n", ntup, psamples);
            }
        } else if (test_id == 201) {
            for (int ntup = 2; ntup <= 5; ntup++){
                int psamples = calculate_psamples(test_id, ntup, file_size);
                printf("    ntuples = %d, suggested psamples are %d\n", ntup, psamples);
            }

        } else if (test_id == 202) {
            for (int ntup = 2; ntup <= 5; ntup++){
                int psamples = calculate_psamples(test_id, ntup, file_size);
                printf("    ntuples = %d, suggested psamples are %d\n", ntup, psamples);
            }

        } else if (test_id == 203) {
            for (int ntup = 0; ntup <= 32; ntup++){
                int psamples = calculate_psamples(test_id, ntup, file_size);
                printf("    ntuples = %d, suggested psamples are %d\n", ntup, psamples);
            }

        } else {
            int psamples = calculate_psamples(test_id, 0, file_size);
            printf("    suggested psample are %d\n", psamples);
        }
    }
    printf("TEST OVER\n");
}