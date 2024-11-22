#include <iostream>
#include <fstream>
#include <string>
#include <unistd.h>
using namespace std;
const char *FILE_NAME = "text.txt";
int main() {
// Check if the file is available for reading
ifstream txt_file;
txt_file.open(FILE_NAME);
if (txt_file.is_open()) {
string line;
while (getline(txt_file, line)) {
cout << "Consumer: " << line << endl;
}
txt_file.close();
} else {
cerr << "Consumer: Could not open file for reading. File may be in use by producer." << endl;
}
return 0;
}
main.cpp
#include <iostream>
#include <cstdlib> // for system()
using namespace std;
int main() {
cout << "Running Producer...\n";
system("./producer"); // Run the producer program
cout << "Running Consumer...\n";
system("./consumer"); // Run the consumer program
cout << "Both Producer and Consumer have finished.\n";
return 0;
}
