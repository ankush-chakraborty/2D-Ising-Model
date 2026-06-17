#include <iostream>
#include <cstdlib>
#include <ctime>

double monteCarloPi(int numIterations) {
    int pointsInCircle = 0;

    for (int i = 0; i < numIterations; i++) {
        // Generate random (x, y) coordinates between 0 and 1
        double x = static_cast<double>(rand()) / RAND_MAX;
        double y = static_cast<double>(rand()) / RAND_MAX;

        // Check if the point is inside the quarter circle
        if ((x * x + y * y) <= 1.0) {
            pointsInCircle++;
        }
    }

    // Calculate Pi as 4 times the ratio of points inside the circle
    return 4.0 * pointsInCircle / numIterations;
}

int main() {
    // Seed the random number generator
    srand(static_cast<unsigned int>(time(0)));

    int numIterations;
    std::cout << "Enter the number of iterations: ";
    std::cin >> numIterations;

    double piEstimate = monteCarloPi(numIterations);
    std::cout << "Estimated value of Pi: " << piEstimate << std::endl;

    return 0;
}
