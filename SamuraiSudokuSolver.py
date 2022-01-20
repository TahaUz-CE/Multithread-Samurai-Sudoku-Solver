import sys
import threading
import time
import matplotlib.pyplot as plt

# Bunu tekrar kontrol et (https://www.geeksforgeeks.org/sudoku-backtracking-7/)
import pygame

M = 9

while True:

    print("Hello")
    file2 = open("SudokuKayıt5Thread.txt","w")
    file3 = open("SudokuKayıt10Thread.txt","w")

    foundTime_5_thread = []
    foundTime_10_thread = []



    def puzzle(a):
        for i in range(M):
            for j in range(M):
                print(a[i][j], end=" ")
            print()


    def solve(grid, grid2, grid3, grid4, grid5, row, col, num, label):
        #     print(row)
        #     print(col)
        #     print(num)

        startRow = row - row % 3
        startCol = col - col % 3

        if label == 1:

            for x in range(9):
                if grid[row][x] == num:
                    return False

            for x in range(9):
                if grid[x][col] == num:
                    return False

            for i in range(3):
                for j in range(3):
                    if grid[i + startRow][j + startCol] == num:
                        return False

            if row > 5 and col > 5:
                for x in range(9):
                    if grid5[row - 6][x] == num:
                        return False

                for x in range(9):
                    if grid5[x][col - 6] == num:
                        return False

                for i in range(0, 3, 1):
                    for j in range(0, 3, 1):
                        if grid5[i][j] == num:
                            return False

        if label == 2:

            for x in range(9):
                if grid2[row][x] == num:
                    return False

            for x in range(9):
                if grid2[x][col] == num:
                    return False

            for i in range(3):
                for j in range(3):
                    if grid2[i + startRow][j + startCol] == num:
                        return False

            if row > 5 and col < 3:
                for x in range(9):
                    if grid5[row - 6][x] == num:
                        return False

                for x in range(9):
                    if grid5[x][col + 6] == num:
                        return False

                for i in range(0, 3, 1):
                    for j in range(6, 9, 1):
                        if grid5[i][j] == num:
                            return False

        if label == 3:

            for x in range(9):
                if grid3[row][x] == num:
                    return False

            for x in range(9):
                if grid3[x][col] == num:
                    return False

            for i in range(3):
                for j in range(3):
                    if grid3[i + startRow][j + startCol] == num:
                        return False

            if row < 3 and col > 5:
                for x in range(9):
                    if grid5[row + 6][x] == num:
                        return False

                for x in range(9):
                    if grid5[x][col - 6] == num:
                        return False

                for i in range(6, 9, 1):
                    for j in range(0, 3, 1):
                        if grid5[i][j] == num:
                            return False
        if label == 4:

            for x in range(9):
                if grid4[row][x] == num:
                    return False

            for x in range(9):
                if grid4[x][col] == num:
                    return False

            for i in range(3):
                for j in range(3):
                    if grid4[i + startRow][j + startCol] == num:
                        return False

            if row < 3 and col < 3:
                for x in range(9):
                    if grid5[row + 6][x] == num:
                        return False

                for x in range(9):
                    if grid5[x][col + 6] == num:
                        return False

                for i in range(6, 9, 1):
                    for j in range(6, 9, 1):
                        if grid5[i][j] == num:
                            return False

        if label == 5:
            for x in range(9):
                if grid5[row][x] == num:
                    return False

            for x in range(9):
                if grid5[x][col] == num:
                    return False

            for i in range(3):
                for j in range(3):
                    if grid5[i + startRow][j + startCol] == num:
                        return False

        return True


    def Suduko(grid, grid2, grid3, grid4, grid5, row, col, label, threadKind, startIndexRC):
        # print("row = ",row)
        # print("col = ",col)

        # if row == 3 and col == 3:
        #     print(grid)
        #     print(grid2)

        if row == M - 1 and col == M:
            # print(threadKind)
            # print(label)
            return True

        if col == M:
            row += 1
            col = 0


        if label == 1:
            if grid[row][col] > 0:
                return Suduko(grid, grid2, grid3, grid4, grid5, row, col + 1, label, threadKind, startIndexRC)
        if label == 2:
            if grid2[row][col] > 0:
                return Suduko(grid, grid2, grid3, grid4, grid5, row, col + 1, label, threadKind, startIndexRC)
        if label == 3:
            if grid3[row][col] > 0:
                return Suduko(grid, grid2, grid3, grid4, grid5, row, col + 1, label, threadKind, startIndexRC)
        if label == 4:
            if grid4[row][col] > 0:
                return Suduko(grid, grid2, grid3, grid4, grid5, row, col + 1, label, threadKind, startIndexRC)
        if label == 5:
            if (row < 3 and col < 3) or (row < 3 and col > 5) or (row > 5 and col < 3) or (row > 5 and col > 5):
                return Suduko(grid, grid2, grid3, grid4, grid5, row, col + 1, label, threadKind, startIndexRC)
            if grid5[row][col] > 0:
                return Suduko(grid, grid2, grid3, grid4, grid5, row, col + 1, label, threadKind, startIndexRC)


        for num in range(1, M + 1, 1):

            if solve(grid, grid2, grid3, grid4, grid5, row, col, num, label):

                if label == 1:
                    if row > 5 and col > 5:
                        grid5[row - 6][col - 6] = num
                    grid[row][col] = num

                if label == 2:
                    if row > 5 and col < 3:
                        grid5[row - 6][col + 6] = num
                    grid2[row][col] = num

                if label == 3:
                    if row < 3 and col > 5:
                        grid5[row + 6][col - 6] = num
                    grid3[row][col] = num

                if label == 4:
                    if row < 3 and col < 3:
                        grid5[row + 6][col + 6] = num
                    grid4[row][col] = num

                if label == 5:
                    grid5[row][col] = num

                if threadKind == 5:
                    end_5 = time.time()
                    if end_5 - start_5 != 0.0:
                        foundTime_5_thread.append((end_5 - start_5))

                if threadKind == 10:
                    end_10 = time.time()
                    if end_10 - start_10 != 0.0:
                        foundTime_10_thread.append((end_10 - start_10))

                if threadKind == 5:
                    Yaz = str(label) + ". Sudokudaki " + str(row) + ".Satir " + str(col) + ".Sutun = " + str(
                        num) + " olarak degisti\n"
                    file2.write(Yaz)
                if threadKind == 10:
                    Yaz = str(label) + ". Sudokudaki " + str(row) + ".Satir " + str(col) + ".Sutun = " + str(
                        num) + " olarak degisti\n"
                    file3.write(Yaz)

                if Suduko(grid, grid2, grid3, grid4, grid5, row, col + 1, label, threadKind, startIndexRC):
                    return True

            if label == 1:
                if row > 5 and col > 5:
                    grid5[row - 6][col - 6] = 0
                grid[row][col] = 0

            if label == 2:
                if row > 5 and col < 3:
                    grid5[row - 6][col + 6] = 0
                grid2[row][col] = 0

            if label == 3:
                if row < 3 and col > 5:
                    grid5[row + 6][col - 6] = 0
                grid3[row][col] = 0

            if label == 4:
                if row < 3 and col < 3:
                    grid5[row + 6][col + 6] = 0
                grid4[row][col] = 0

            if label == 5:
                grid5[row][col] = 0

        return False


    # Reading SamuraiSudoku.txt

    board1 = []
    board2 = []
    board3 = []
    board4 = []
    board5 = []
    board6 = []
    board7 = []
    board8 = []
    board9 = []
    board10 = []

    # print(SamuraiSudoku)

    # Board 1

    file = open("SamuraiSudoku.txt")

    for j in range(9):
        SamuraiSudoku = file.readline()
        # print(SamuraiSudoku)

        temp = []
        temp2 = []
        for i in range(9):
            # print(i)
            if SamuraiSudoku[i] == "*":
                temp.append(0)
                temp2.append(0)
            elif SamuraiSudoku[i] != "\n":
                temp.append(int(SamuraiSudoku[i]))
                temp2.append(int(SamuraiSudoku[i]))
        board1.append(temp)
        board6.append(temp2)

    file.close()
    # print(board6)
    # print(board1)

    # Board 2

    file = open("SamuraiSudoku.txt")

    for j in range(9):
        SamuraiSudoku = file.readline()
        # print(SamuraiSudoku)
        a = 9
        b = 18
        if j > 5:
            a = 12
            b = 21
        temp = []
        temp2 = []
        for i in range(a, b, 1):
            # print(i)
            if SamuraiSudoku[i] == "*":
                temp.append(0)
                temp2.append(0)
            elif SamuraiSudoku[i] != "\n":
                temp.append(int(SamuraiSudoku[i]))
                temp2.append(int(SamuraiSudoku[i]))
        board2.append(temp)
        board7.append(temp2)
    file.close()

    # print(board2)

    # Board 3

    file = open("SamuraiSudoku.txt")

    for j in range(21):
        SamuraiSudoku = file.readline()
        # print(SamuraiSudoku)

        if j > 11:
            temp = []
            temp2 = []
            for i in range(9):
                # print(i)
                if SamuraiSudoku[i] == "*":
                    temp.append(0)
                    temp2.append(0)
                elif SamuraiSudoku[i] != "\n":
                    temp.append(int(SamuraiSudoku[i]))
                    temp2.append(int(SamuraiSudoku[i]))
            board3.append(temp)
            board8.append(temp2)
    file.close()

    # print(board3)

    # Board 4

    file = open("SamuraiSudoku.txt")

    for j in range(21):
        SamuraiSudoku = file.readline()
        # print(SamuraiSudoku)

        if j > 11:
            a = 12
            b = 21

            if j > 14:
                a = 9
                b = 18
            temp = []
            temp2 = []
            for i in range(a, b, 1):
                # print(i)
                if SamuraiSudoku[i] == "*":
                    temp.append(0)
                    temp2.append(0)
                elif SamuraiSudoku[i] != "\n":
                    temp.append(int(SamuraiSudoku[i]))
                    temp2.append(int(SamuraiSudoku[i]))
            board4.append(temp)
            board9.append(temp2)
    file.close()

    # print(board4)

    # Board 5

    file = open("SamuraiSudoku.txt")

    for j in range(21):
        SamuraiSudoku = file.readline()
        # print(SamuraiSudoku)

        if j > 5 and j < 15:

            a = 0
            b = 9
            if j < 9 or j > 11:
                a = 6
                b = 15

            temp = []
            temp2 = []
            for i in range(a, b, 1):
                # print(i)
                if SamuraiSudoku[i] == "*":
                    temp.append(0)
                    temp2.append(0)
                elif SamuraiSudoku[i] != "\n":
                    temp.append(int(SamuraiSudoku[i]))
                    temp2.append(int(SamuraiSudoku[i]))
            board5.append(temp)
            board10.append(temp2)
    file.close()


    # print(board5)

    def s1():
        Suduko(board1, board2, board3, board4, board5, 0, 0, 1, 5, 0)


    def s2():
        Suduko(board1, board2, board3, board4, board5, 0, 0, 2, 5, 0)


    def s3():
        Suduko(board1, board2, board3, board4, board5, 0, 0, 3, 5, 0)


    def s4():
        Suduko(board1, board2, board3, board4, board5, 0, 0, 4, 5, 0)


    def s5():
        Suduko(board1, board2, board3, board4, board5, 0, 0, 5, 5, 0)

    start = time.time()

    start_5 = time.time()

    start_0 = time.time()

    t1 = threading.Thread(target=s1)
    t1.start()

    start_1 = time.time()
    t2 = threading.Thread(target=s2)
    t2.start()

    start_2 = time.time()
    t3 = threading.Thread(target=s3)
    time.sleep(1)
    t3.start()

    start_3 = time.time()
    t4 = threading.Thread(target=s4)
    time.sleep(1)
    t4.start()

    start_4 = time.time()
    t5 = threading.Thread(target=s5)
    time.sleep(0.1)
    t5.start()

    end = time.time()

    # print(board1)
    # print(board6)

    time.sleep(3)

    # print("******************************************************")
    # print("5 Thread ile Samurai Sudoku")
    # print("******************************************************")
    # puzzle(board1)
    # print("******************************************************")
    # puzzle(board2)
    # print("******************************************************")
    # puzzle(board3)
    # print("******************************************************")
    # puzzle(board4)
    # print("******************************************************")
    # puzzle(board5)
    #
    #
    # print("******************************************************")
    # print("10 Thread ile Samurai Sudoku")
    # print("******************************************************")
    # puzzle(board6)
    # print("******************************************************")
    # puzzle(board7)
    # print("******************************************************")
    # puzzle(board8)
    # print("******************************************************")
    # puzzle(board9)
    # print("******************************************************")
    # puzzle(board10)
    # print("******************************************************")

    def s1_1():
        Suduko(board6, board7, board8, board9, board10, 0, 0, 1, 10, 0)


    def s1_2():
        Suduko(board6, board7, board8, board9, board10, 4, 4, 1, 10, 4)


    def s2_1():
        Suduko(board6, board7, board8, board9, board10, 0, 0, 2, 10, 0)


    def s2_2():
        Suduko(board6, board7, board8, board9, board10, 4, 4, 2, 10, 4)


    def s3_1():
        Suduko(board6, board7, board8, board9, board10, 0, 0, 3, 10, 0)


    def s3_2():
        Suduko(board6, board7, board8, board9, board10, 4, 4, 3, 10, 4)


    def s4_1():
        Suduko(board6, board7, board8, board9, board10, 0, 0, 4, 10, 0)


    def s4_2():
        Suduko(board6, board7, board8, board9, board10, 4, 4, 4, 10, 4)


    def s5_1():
        Suduko(board6, board7, board8, board9, board10, 0, 0, 5, 10, 0)


    def s5_2():
        Suduko(board6, board7, board8, board9, board10, 4, 4, 5, 10, 4)


    start2 = time.time()

    start_10 = time.time()

    start_0_1 = time.time()

    t1_1 = threading.Thread(target=s1_1)
    t1_1.start()
    time.sleep(0.1)

    start_0_2 = time.time()

    t1_2 = threading.Thread(target=s1_2)
    t1_2.start()

    t2_1 = threading.Thread(target=s2_1)
    t2_1.start()
    time.sleep(1)

    t2_2 = threading.Thread(target=s2_2)
    t2_2.start()

    t3_1 = threading.Thread(target=s3_1)
    t3_1.start()

    t3_2 = threading.Thread(target=s3_2)
    t3_2.start()
    time.sleep(1)

    t4_1 = threading.Thread(target=s4_1)
    t4_1.start()

    t4_2 = threading.Thread(target=s4_2)
    t4_2.start()
    time.sleep(1)

    t5_1 = threading.Thread(target=s5_1)
    t5_1.start()

    t5_2 = threading.Thread(target=s5_2)
    t5_2.start()

    end2 = time.time()

    print("5 Thread = ", len(foundTime_5_thread))
    print("10 Thread = ", len(foundTime_10_thread))

    # print("******************************************************")
    # print("5 Thread ile Samurai Sudoku")
    # print("******************************************************")
    # puzzle(board1)
    # print("******************************************************")
    # puzzle(board2)
    # print("******************************************************")
    # puzzle(board3)
    # print("******************************************************")
    # puzzle(board4)
    # print("******************************************************")
    # puzzle(board5)
    #
    # print("******************************************************")
    # print("5 Thread ile Samurai Sudoku = ", end - start - 2.1, "sn")
    # print("******************************************************\n")
    #
    # print("******************************************************")
    # print("10 Thread ile Samurai Sudoku")
    # print("******************************************************")
    # puzzle(board6)
    # print("******************************************************")
    # puzzle(board7)
    # print("******************************************************")
    # puzzle(board8)
    # print("******************************************************")
    # puzzle(board9)
    # print("******************************************************")
    # puzzle(board10)
    # print("******************************************************")
    # print("10 Thread ile Samurai Sudoku = ", end2 - start2 - 3.1, "sn")
    # print("******************************************************\n")

    kontrol = True
    for i in range(9):
        for j in range(9):
            if board1[i][j] == 0 or board2[i][j] == 0 or \
                    board3[i][j] == 0 or board4[i][j] == 0 or \
                    board5[i][j] == 0 or board6[i][j] == 0 or \
                    board7[i][j] == 0 or board8[i][j] == 0 or \
                    board9[i][j] == 0 or board10[i][j] == 0:

                kontrol = False


    if kontrol:
        print("Girdi")

        file2.close()
        file3.close()

        print("******************************************************")
        print("5 Thread ile Samurai Sudoku")
        print("******************************************************")
        puzzle(board1)
        print("******************************************************")
        puzzle(board2)
        print("******************************************************")
        puzzle(board3)
        print("******************************************************")
        puzzle(board4)
        print("******************************************************")
        puzzle(board5)

        print("******************************************************")
        print("5 Thread ile Samurai Sudoku = ", end - start - 2.1, "sn")
        print("******************************************************\n")

        print("******************************************************")
        print("10 Thread ile Samurai Sudoku")
        print("******************************************************")
        puzzle(board6)
        print("******************************************************")
        puzzle(board7)
        print("******************************************************")
        puzzle(board8)
        print("******************************************************")
        puzzle(board9)
        print("******************************************************")
        puzzle(board10)
        print("******************************************************")
        print("10 Thread ile Samurai Sudoku = ", end2 - start2 - 3.1, "sn")
        print("******************************************************\n")

        for i in range(15):
            print(foundTime_5_thread[i])
        print(len(foundTime_5_thread))

        for i in range(15):
            print(foundTime_10_thread[i])
        print(len(foundTime_10_thread))

        bul_kare_sayi = []
        bul_sure = []
        temp_i = 0.0
        for i in foundTime_5_thread:
            if i != temp_i:

                if 3 > i > 2:
                    bul_kare_sayi.append(foundTime_5_thread.count(i - 2))
                    bul_sure.append(i - 2.1)
                elif 2 > i > 1:
                    bul_kare_sayi.append(foundTime_5_thread.count(i - 1))
                    bul_sure.append(i - 1.1)
                else:
                    bul_kare_sayi.append(foundTime_5_thread.count(i))
                    bul_sure.append(i)
                temp_i = i

        print(len(bul_kare_sayi))
        print(len(bul_sure))

        print(bul_kare_sayi[0])
        print(bul_sure[0])

        bul_kare_sayi2 = []
        bul_sure2 = []
        temp_i2 = 0.0

        for i in foundTime_10_thread:
            if i != temp_i2:

                if 4 > i > 3:
                    bul_kare_sayi2.append(foundTime_10_thread.count(i - 3.1))
                    bul_sure2.append(i - 3.1)

                elif 3 > i > 2:
                    bul_kare_sayi2.append(foundTime_10_thread.count(i - 2.1))
                    bul_sure2.append(i - 2.1)

                elif 2 > i > 1:
                    bul_kare_sayi2.append(foundTime_10_thread.count(i - 1.1))
                    bul_sure2.append(i - 1.1)

                else:
                    bul_kare_sayi2.append(foundTime_10_thread.count(i))
                    bul_sure2.append(i)

                temp_i2 = i

        print(len(bul_kare_sayi2))
        print(len(bul_sure2))

        print(bul_kare_sayi2[0])
        print(bul_sure2[0])

        # Grafik

        plt.plot(bul_sure, bul_kare_sayi, color="red", label="5 Thread")
        plt.plot(bul_sure2, bul_kare_sayi2, color="yellow", label="10 Thread")
        plt.title("Samurai Sudoku Grafiği (Kare Bulma/Zaman)")
        plt.xlabel("Sure")
        plt.ylabel("Kare Sayisi")
        plt.legend()
        plt.show()


        # Arayüz

        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        WINDOW_HEIGHT = 441
        WINDOW_WIDTH = 441

        global SCREEN, CLOCK
        pygame.init()
        SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        CLOCK = pygame.time.Clock()
        SCREEN.fill(WHITE)

        while True:

            blockSize = 21  # Set the size of the grid block
            i = 0
            i_2 = 0
            j = 0
            k = 0
            t = 3
            t_1 = 0
            #k_1 = 3
            for x in range(0, WINDOW_WIDTH, blockSize):
                k_1 = 3
                for y in range(0, WINDOW_HEIGHT, blockSize):
                    rect = pygame.Rect(x, y, blockSize, blockSize)

                    if 232 > x > 188 and 108 > y > -22:
                        pygame.draw.rect(SCREEN, WHITE, rect, 1)
                    elif 441 - 189 > x > 441 - 232 - 21 and 441 + 22 > y > 441 - 108 - 21:
                        pygame.draw.rect(SCREEN, WHITE, rect, 1)
                    elif 441 + 22 > x > 441 - 108 - 21 and 441 - 189 > y > 441 - 232 - 21:
                        pygame.draw.rect(SCREEN, WHITE, rect, 1)
                    elif 108 > x > -22 and 232 > y > 188:
                        pygame.draw.rect(SCREEN, WHITE, rect, 1)
                    else:
                        pygame.draw.rect(SCREEN, BLACK, rect, 1)
                        myfont = pygame.font.SysFont('Arial', 15)
                        if y < 21 * 9 and x < 21 * 9:
                            textsurface = myfont.render(str(board1[i][j]), False, (0, 0, 0))
                            j += 1
                            j %= 9
                            SCREEN.blit(textsurface, (y + 5, x))
                        elif y > 21 * 11 and x < 21 * 9:
                            textsurface = myfont.render(str(board2[i][j]), False, (0, 0, 0))
                            j += 1
                            j %= 9
                            SCREEN.blit(textsurface, (y + 5, x))
                        elif y > 21 * 11 and x > 21 * 11:
                            textsurface = myfont.render(str(board4[i - 3][j]), False, (0, 0, 0))
                            j += 1
                            j %= 9
                            SCREEN.blit(textsurface, (y + 5, x))
                        elif y < 21 * 9 and x > 21 * 11:
                            textsurface = myfont.render(str(board3[i - 3][j]), False, (0, 0, 0))
                            j += 1
                            j %= 9
                            SCREEN.blit(textsurface, (y + 5, x))
                        elif 21 * 15 > y > 21 * 5 and 21 * 15 > x > 21 * 5:

                            if 21 * 12 > y > 21 * 8:
                                textsurface = myfont.render(str(board5[k][k_1]), False, (0, 0, 0))
                                SCREEN.blit(textsurface, (y + 5, x))
                                k_1 += 1
                                if(k_1 == 6):
                                    k +=1
                            if 21 * 12 > x > 21 * 8:
                                textsurface = myfont.render(str(board5[t][t_1]), False, (0, 0, 0))
                                SCREEN.blit(textsurface, (y + 5, x))
                                t_1 += 1
                                if(t_1 == 9):
                                    t +=1
                                    t_1 = 0



                i += 1
                i %= 9

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

        break
