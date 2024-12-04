char increased(char ch);
bool similar(char lhs, char rhs);

bool canMakeSubsequence(char* str1, char* str2) {
    char* rit = str2;

    for (char* lit = str1; *lit && *rit; ++lit) {
        if (similar(*lit, *rit)) {
            ++rit;
        }
    }

    return *rit == '\0';
}

char increased(char ch) {
    int idx = ch - 'a';
    return (idx + 1) % 26 + 'a';
}

bool similar(char lhs, char rhs) {
    return lhs == rhs || increased(lhs) == rhs;
}