#include <iostream>
#include <cmath>

using namespace std;

unsigned char LR1_calculation(float x, float y, float a, float b, float R) {
    if (a <= b) {
        cout << "Ошибка: a должно быть больше b!" << endl;
        return 4;
    }
    if (sqrt(x * x + y * y) > R)
        return 0;
    if (y > a)
        return 1;
    if (y > b)
        return 2;
    return 3;
}

int main() {
    float x, y, a, b, R;
    cout << "Введите координаты точки (x, y): ";
    cin >> x >> y;
    cout << "Введите значения a, b, R: ";
    cin >> a >> b >> R;
    
    unsigned char region = LR1_calculation(x, y, a, b, R);
    if (region != 4) 
        cout << "Точка находится в области: " << (int)region << endl;
    return 0;
}
