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

        List<List<Integer>> viajeros = new ArrayList<>(); // Lista de listas de viajeros que llegan en X tiempo al planeta n


        for (int i = 0; i < n; i++){
            List<Integer> viajeros_por_planeta = new ArrayList<>(); // Lista de viajeros en X planeta
            
            int cantidad_viajeros = sc.nextInt();                   // Cantidad de viajeros en X planeta
            for (int j = 0; j < cantidad_viajeros; j++){            
                int segundos_planeta = sc.nextInt();                // Agrego los segundos de aparicion de los viajeros
                viajeros_por_planeta.add(segundos_planeta);         // Agrego al viajero a la lista de su planeta
            }
            viajeros.add(viajeros_por_planeta);                     // Agrego la lista del planeta a la lista de planetas
        }
        
        sc.close();

        viajeMinimo(grafo, viajeros);

    }

    static void viajeMinimo(List<List<Arista>> grafo, List<List<Integer>> viajeros){
        for (int i = 0; i < grafo.size(); i++) {
            System.out.print("Planeta " + (i + 1) + ": ");
            for (Arista arista : grafo.get(i)) {
                System.out.print("-> (Planeta " + (arista.destino + 1) + ", segundos: " + arista.peso + ") ");
            }
            System.out.println();
        }

        for (int i = 0; i < viajeros.size(); i++){
            System.out.println("Viajeros por planeta: " + viajeros.get(i));
        }
    }
}
