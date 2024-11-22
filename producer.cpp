#include <iostream>
#include <fstream> // Include for file operations
using namespace std;
int main() {
srand(time(0)); // Initialize random seed
int random_data = rand() % 100; // Generate random data
// Open file in append mode
ofstream txt_file("text.txt", ios::app);
// Check if the file is successfully opened
if (txt_file.is_open()) {
// Write text to the file
txt_file << "Producer wrote: " << random_data << endl;
cout << "Producer: Data " << random_data << " written to the file." << endl;
txt_file << "This is the first assignment and a text written by the producer.\n";
cout << "Text successfully written to the file.\n";
// Close the file after writing
txt_file.close();
} else {
cerr << "Error: Could not open file for writing.\n";
}
return 0;
}
