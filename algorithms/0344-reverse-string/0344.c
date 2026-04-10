void reverseString(char* s, int tam) {
    for (int i = 0;;i++) {
        if (i >= tam -1 -i) {
            break;
        }
        
        char temp = s[i];
        s[i] = s[tam -1 -i];
        s[tam -1 -i] = temp;
    }
}