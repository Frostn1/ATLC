#include "../inc/Tool.h"

bool isSpace(char c)  {
    return c == SPACE_ASCII ||  c == TAB_ASCII || c == NEWLINE_ASCII || c == CARRIAGERETURN_ASCII;
}