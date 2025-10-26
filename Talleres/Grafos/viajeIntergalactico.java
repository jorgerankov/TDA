import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class viajeIntergalactico {
    static class Arista {
        int destino;
        int peso;
        Arista(int destino, int peso) {
            this.destino = destino;
            this.peso = peso;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        List<List<Arista>> grafo = new ArrayList<>();
        for (int i = 0; i < n; i++){
            grafo.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++){
            int planeta_a = sc.nextInt();
            int planeta_b = sc.nextInt();
            int segundos = sc.nextInt();

            // Uso indices de 0 a n - 1 para el digrafo (cada planeta a apunta a un planeta b en S segundos)
            grafo.get(planeta_a - 1).add(new Arista(planeta_b - 1, segundos));
        }
        sc.close();

        viajeMinimo(grafo);
    }

    static void viajeMinimo(List<List<Arista>> grafo){
        for (int i = 0; i < grafo.size(); i++) {
            System.out.print("Planeta " + (i + 1) + ": ");
            for (Arista arista : grafo.get(i)) {
                System.out.print("-> (Planeta " + (arista.destino + 1) + ", segundos: " + arista.peso + ") ");
            }
            System.out.println();
        }
    }
}
