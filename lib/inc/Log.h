#ifndef LOG_H
#define LOG_H

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

FILE* logP;

void _Log(char* path);
void writeLog(char* msg);
void LogF();

#endif // !LOG_H