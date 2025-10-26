import java.util.*;

// La restriccion es <= 10^5 asi que uso Int
public class maquinaMisteriosa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.close();
        System.out.println(caminoMinimo(n, m));
    }

    static int caminoMinimo(int n, int m) {
        if (n >= m) return n - m;
        
        Queue<int[]> cola = new LinkedList<>();     // Cola para guardar los pares (valor, pasos)
        boolean[] visitados = new boolean[20001];   // Array con costo <= 10^5 para guardar los valores visitados 
        
        cola.add(new int[]{n, 0});                  // Agrego primer valor (n) a la cola
        visitados[n] = true;                        // Lo marco como visitado
        
        while (!cola.isEmpty()) {                   // Mientras queden valores por visitar
            int[] par = cola.poll();                // Obtengo el par (valor, pasos) actual
            int valor = par[0];                     // Variable para el valor actual
            int pasos = par[1];                     // Variable para el paso que estoy haciendo
            
            // Multiplicar por 2
            int mult = valor * 2;                   // Variable para el valor actual * 2
            if (mult == m) return pasos + 1;        // Si encontre el valor, devuelvo la cantidad total de pasoss
            if (mult < 20001 && !visitados[mult]) { // Si no me paso de 10^5 y no visite el valor * 2:
                visitados[mult] = true;             // Lo marco como visitado
                cola.add(new int[]{mult, pasos + 1}); // Agrego el valor para analizar luego su doble y su anterior a la cola
            }
            
            // Restar 1
            int menos_uno = valor - 1;              // Variable para el valor actual - 1
            if (menos_uno == m) return pasos + 1;   // Si encontre el valor, devuelvo la cantidad total de pasoss
            if (menos_uno > 0 && !visitados[menos_uno]) { // Si no me paso de 10^5 y no visite el valor - 1:
                visitados[menos_uno] = true;        // Lo marco como visitado
                cola.add(new int[]{menos_uno, pasos + 1}); // Agrego el valor para analizar luego su doble y su anterior a la cola
            }
        }
        
        return -1;  // Si no se cumple ninguna de las condiciones (se descompone) devuelvo -1
    }
}