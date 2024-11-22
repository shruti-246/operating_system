#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <fcntl.h>
#include <string.h>
#define FILENAME "assignment02.txt"
pid_t prod_pid;
pid_t cons_pid;
//consumer signal handler
void cons_sig_hand(int signum) {
//just for calling the function
}
//producer signal handler
void prod_sig_hand(int signum) {
//just for calling the function
}
//Function of the producer
void producer() {
while (1) {
//waiting for the signal from consumer
printf("Producer waiting for consumer signal...\n");
pause();
//open the file to write data
int fd = open(FILENAME, O_WRONLY | O_CREAT | O_TRUNC, 0666);//file handling
if (fd < 0) {
perror("Failed to open file");
exit(EXIT_FAILURE);//terminating when it finish
}
//writing data to the file
const char *text_written = "Dinner's Ready!\n";
write(fd, text_written, strlen(text_written));
printf("Producer: Wrote data to file.\n");
//sending signal to the consumer that data is ready
printf("Producer sending signal to consumer...\n");
kill(cons_pid, SIGUSR1);//sending signals without terminating
}
}
//function of the consumer
void consumer() {
while (1) {
//waiting for the signal from producer
printf("Consumer waiting for producer signal...\n");
pause();
//once the signal is received by the consumer
printf("Consumer: Received signal\n");
//open the file to read the data written by the producer
int fd = open(FILENAME, O_RDONLY);//file handling
if (fd < 0) {
perror("Failed to open file");
exit(EXIT_FAILURE);//terminating the process when finish
}
char buffer[256];
ssize_t text_read = read(fd, buffer, sizeof(buffer) - 1);
if (text_read > 0) {
buffer[text_read] = '\0'; //null terminator
printf("Consumer: Read from file: %s", buffer);
}
close(fd);
//deleting data from the file (truncate it)
fd = open(FILENAME, O_WRONLY | O_TRUNC); //file handling
if (fd < 0) {
perror("Failed to open file for truncation");
exit(EXIT_FAILURE);//terminating the process when finish
}
close(fd);
printf("Consumer: Cleared data from file.\n");
//sending the signal to the producer that data has been consumed by this
message
printf("Consumer: I'm Still Hungry\n");
printf("Consumer sending signal to producer...\n");
kill(prod_pid, SIGUSR2);//sending signals without terminating
}
}
//the parent function
void parent() {
//set up the signal handlers
signal(SIGUSR1, cons_sig_hand);
signal(SIGUSR2, prod_sig_hand);
//producer and consumer processes
prod_pid = fork();
if (prod_pid == 0) {
//running the producer process
producer();
exit(0);//teminating when the process is finish
}
cons_pid = fork();
if (cons_pid == 0) {
//running the consumer process
consumer();
exit(0);//terminating the process
}
//for this program the consumer is going to start first
sleep(1); //time for consumer to start and wait
//sending signal to the consumer to start
kill(cons_pid, SIGUSR2);//sending signals without terminating
//parent process waits indefinitely
while (1) {
pause(); //wait for any signal
}
}
int main() {
parent();
return 0;
}
