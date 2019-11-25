import org.junit.Test;

import static junit.framework.TestCase.assertEquals;

public class TestMyStrings {
  MyStrings obj = new MyStrings();

  @Test
  public void testCat(){
    char[] test = {'c', ' ', 'a', ' ', 't', ' ', ' ', ' ', ' '};
    obj.urlify(test, 5);
    String rv = new String(test);
    assertEquals("c%20a%20t", rv);
  }

  @Test
  public void testSimple() {
    char[] empty = {};
    obj.urlify(empty, 0);
    String rv = new String(empty);
    assertEquals("", rv);
  }

  @Test
  public void testSimple2() {
    char[] mark = {'m', 'a', 'r', 'k'};
    obj.urlify(mark, 4);
    String rv = new String(mark);
    assertEquals("mark", rv);
  }

  @Test
  public void testBookExample() {
    char[] ex = {'M', 'r', ' ', 'J', 'o', 'h', 'n', ' ', 'S', 'm', 'i', 't', 'h', ' ', ' ', ' ',
            ' '};
    obj.urlify(ex, 13);
    String rv = new String(ex);
    assertEquals("Mr%20John%20Smith", rv);
  }

  @Test
  public void testSpace() {
    char[] ex = {' ', ' ', ' '};
    obj.urlify(ex, 1);
    String rv = new String(ex);
    assertEquals("%20", rv);
  }

  @Test
  public void testSpace2() {
    char[] ex = {' ', ' ', ' ', ' ', ' ', ' '};
    obj.urlify(ex, 2);
    String rv = new String(ex);
    assertEquals("%20%20", rv);
  }
}
