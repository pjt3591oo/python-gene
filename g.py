from random import random
from echo import Ecosystem as Echo
import time

if __name__ == "__main__":
    option1 = {
                "gene_count" : 30,
                "gene_length" : 6,
                "mutation_probability" : 0.1
            }
    echo = Echo(option1)

    while echo.is_continue():
        print('=======================')
        print(str(echo.generation) +'세대 유전자들')
        echo.next_generation()

        print(str(echo.generation - 1) +'세대 상위 유전자')
        for parent in echo.parents:
            print(parent.status, parent.similar)

        print('=======================\n\n')
        time.sleep(1)
