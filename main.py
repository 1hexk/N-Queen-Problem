import N_queen_problem as state
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

while True:
    print("Choose an option:")
    print("1. algorithm")
    print("2. test algorithm")
    print("3. Quit")
    menu = int(input())
    if menu == 1:
        while True:
            print("Choose an option:")
            print("1. Solve 8 queens problem")
            print("2. Solve custom n queens problem")
            print("3. Quit")
            choice = int(input())

            if choice == 1:
                n = 8
            elif choice == 2:
                n = int(input("Enter the number of queens: "))
            elif choice == 3:
                break
            else:
                print("Invalid choice")
                continue

            initial_state = state.State.random_state(n)

            print("Choose a search algorithm:")
            print("1. Breadth-first search (BFS)")
            print("2. Depth-first search (DFS)")
            print("3. Greedy search")
            print("4. A* search")
            search_choice = int(input())

            if search_choice == 1:
                print("initial_state :", initial_state.queens)
                state.PrintBoard(initial_state.queens)
                solution, steps, search_cost, max_fringe_size = state.BFS(initial_state)
            elif search_choice == 2:
                print("initial_state :", initial_state.queens)
                state.PrintBoard(initial_state.queens)
                solution, steps, search_cost, max_fringe_size = state.DFS(initial_state)
            elif search_choice == 3:
                print("initial_state :", initial_state.queens)
                print("initial State heuristic:", initial_state.heuristic())
                state.PrintBoard(initial_state.queens)
                solution, steps, search_cost, max_fringe_size = state.greedy(initial_state)
            elif search_choice == 4:
                print("initial_state :", initial_state.queens)
                print("initial State heuristic:", initial_state.heuristic())
                state.PrintBoard(initial_state.queens)
                solution, steps, search_cost, max_fringe_size = state.Astar(initial_state)
            else:
                print("Invalid choice")
                continue

            if solution is not None:
                print("Solution found:", solution.queens)
                state.PrintBoard(solution.queens)
            else:
                print("No solution found")
            state.printinfo(steps, search_cost, max_fringe_size)
    if menu == 2:
        while True:
            i = 1
            BFS = []
            DFS = []
            greedy = []
            astar = []
            itr = int(input("Enter the number of iterations: "))
            n = int(input("Enter the number of Queens (0 to quit): "))
            if n == 0:
                break
            while i <= n:
                BFS_avg, DFS_avg, greedy_avg, astar_avg = 0, 0, 0, 0

                for _ in range(itr):  # Run each method itr times
                    initial_state = state.State.random_state(i)

                    start = datetime.now()
                    state.BFS(initial_state)
                    end = datetime.now()
                    BFS_avg += (end - start).total_seconds()

                    start = datetime.now()
                    state.DFS(initial_state)
                    end = datetime.now()
                    DFS_avg += (end - start).total_seconds()

                    start = datetime.now()
                    state.greedy(initial_state)
                    end = datetime.now()
                    greedy_avg += (end - start).total_seconds()

                    start = datetime.now()
                    state.Astar(initial_state)
                    end = datetime.now()
                    astar_avg += (end - start).total_seconds()

                # Calculate the average times
                BFS.append((BFS_avg / itr))
                DFS.append((DFS_avg / itr))
                greedy.append((greedy_avg / itr))
                astar.append((astar_avg / itr))

                i += 1

            x_values = list(range(1, i))


            def add_labels(bars, ax1):
                for bar in bars:
                    height = bar.get_height()
                    ax1.annotate(
                        '{:.2f}'.format(height),
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom',
                        fontsize=8
                    )


            width = 0.2
            x_indices = np.arange(len(x_values))
            fig, ax = plt.subplots()

            bars_bfs = ax.bar(x_indices - width * 1.5, BFS, width, label='BFS')
            bars_dfs = ax.bar(x_indices - width * 0.5, DFS, width, label='DFS')
            bars_greedy = ax.bar(x_indices + width * 0.5, greedy, width, label='Greedy')
            bars_astar = ax.bar(x_indices + width * 1.5, astar, width, label='A*')

            add_labels(bars_bfs, ax)
            add_labels(bars_dfs, ax)
            add_labels(bars_greedy, ax)
            add_labels(bars_astar, ax)

            plt.xlabel('Number of Queens')
            plt.ylabel('Execution Time (s)')
            plt.title('Execution Time of Search Algorithms')
            plt.legend()

            plt.xticks(x_indices, x_values)

            plt.show()
    if menu == 3:
        break
