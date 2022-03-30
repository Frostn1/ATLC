#include "../inc/Log.h"

void _Log(char* path) {
    if (logP) return;
    logP = fopen(path, "w+");
}

void writeLog(char* msg) {
    if (!logP) return;
    printf("Hey %s", msg);
    fwrite(msg, sizeof(char), strlen(msg), logP);
}

void LogF() {
    fclose(logP);
}