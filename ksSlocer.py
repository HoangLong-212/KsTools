from ortools.algorithms import pywrapknapsack_solver
import time

# Create list of test cases
testCases = ['n00050', 'n00100' , 'n00200', 'n00500', 'n01000']
# problems = ['00Uncorrelated','01WeaklyCorrelated','02StronglyCorrelated','03InverseStronglyCorrelated', '04AlmostStronglyCorrelated', '05SubsetSum', '06UncorrelatedWithSimilarWeights', '07SpannerUncorrelated', '08SpannerWeaklyCorrelated','09SpannerStronglyCorrelated', '10MultipleStronglyCorrelated','11ProfitCeiling', '12Circle']

# testCases = ['n00050']
problems = ['02StronglyCorrelated']


def main():
    for problem in problems:
        for testCase in testCases:
            filePath = "kplib/" + problem + '/' + testCase + '/' + 'R01000' + '/s006.kp'

            capacities = []
            values = []
            weights = [[]]
            with open(filePath, 'r') as file:
                lines = file.read().splitlines()
                capacities.append(int(lines[2]))
                itemLines = lines[4:]
                for line in itemLines:
                    itemData = line.split()
                    values.append(int(itemData[0]))
                    weights[0].append(int(itemData[1]))

            start = time.time()
        
            # Create the solver
            solver = pywrapknapsack_solver.KnapsackSolver(
                pywrapknapsack_solver.KnapsackSolver.
                KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

            solver.Init(values, weights, capacities)

            # 3 minutes (180 seconds)
            solver.set_time_limit(180.0)
            computed_value = solver.Solve()

            packedItems = []
            packedWeights = []
            totalWeight = 0
            for i in range(len(values)):
                if solver.BestSolutionContains(i):
                    packedItems.append(i)
                    packedWeights.append(weights[0][i])
                    totalWeight += weights[0][i]

            elapsed = time.time() - start

            with open('result.txt', 'a') as file:
                file.write('\nSolution for test case: ' +
                           problem + '/' + testCase)
                file.write('\nRun time: {} sec'.format(elapsed))
                file.write('\nCapacity: {} '.format(str(capacities[0])))
                file.write('\nTotal value: ' + str(computed_value))
                file.write('\nTotal weight: ' + str(totalWeight))
                file.write('\nNumber of items: {} '.format(
                    str(len(packedItems))))
                file.write('\nPacked items: ' + str(packedItems))
                file.write('\nPacked_weights: ' + str(packedWeights))
                file.write('\n-------------------------')

        print('Problem: ' + problem + ' | ' + 'Test Case: ' + testCase + ' completed')
    file.close()


if __name__ == '__main__':
    main()
