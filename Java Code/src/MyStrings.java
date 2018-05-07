public class MyStrings {

  // helper function
  private void insert(char[] str, int index, String toAdd) {
    for (char c : toAdd.toCharArray()) {
      str[index] = c;
      index++;
    }
  }

  // 1.3 cracking the code
  public void urlify(char[] str, int len){
    int spaces = 0; // number of spaces in str
    for (int i = len - 1; i >= 0; i--) {
      if (str[i] == ' ') {
        spaces ++;
      }
    }
    int shift = spaces * 2;
    for (int i = len - 1; i >= 0 && shift >= 0; i--) {
      char curChar = str[i];
      //System.out.println(curChar);
      if (curChar == ' '){
        shift -= 2;
        insert(str, i + shift, "%20");

      } else {
        //System.out.printf("i = %d, shift_amt = %d currChar = %c \n",i, shift, curChar  );
        str[i+shift] = curChar;
      }
    }
  }
}
