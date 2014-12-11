
/* Approximates the value of machine epsilon, the maximum
 * error in binary representation of floating point numbers.
 * 
 * @author Mitch Rees-Jones
 * @created 3/25/2014
 * @modified 12/11/2014
 */
public class Epsilon {
  
  // Initial value of epsilon.
  private static float epsilon = 1.0f;
  
  /* Takes epsilon and divides it by 2 until the error in
   * binary floating point approximates it as 0.
   */
  public static float approximateMachineEpsilon() {
    while((1.0 + (epsilon/2.0)) != 1.0) {
      epsilon /= 2.0f;
    }
    return epsilon;
  }
  
  
  public static void main(String[] args) {
    // My machine approximates epsilon to be 2.220446E-16.
    // Results vary across architectures.
    System.out.println(approximateMachineEpsilon());
  }
}