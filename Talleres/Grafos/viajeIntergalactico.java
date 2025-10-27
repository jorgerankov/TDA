import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Arrays;

public class viajeIntergalactico {
    static class Arista {
        int destino, peso;
        Arista(int destino, int peso) {
            this.destino = destino;
            this.peso = peso;
        }
    }

    static class Nodo implements Comparable<Nodo> {
        int id;
        int distancia;
        
        Nodo(int id, int distancia) {
            this.id = id;
            this.distancia = distancia;
        }
        
        @Override
        public int compareTo(Nodo otro) {
            return Integer.compare(this.distancia, otro.distancia);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        List<List<Arista>> grafo = new ArrayList<>();
        for (int i = 0; i < n; i++){
            grafo.add(new ArrayList<>());                   // Agrego una lista de planetas que conectan con i
        }

        for (int i = 0; i < m; i++){
            int planeta_a = sc.nextInt();                   // Defino los pares de planetas con sus segundos
            int planeta_b = sc.nextInt();                   // Defino los pares de planetas con sus segundos
            int segundos = sc.nextInt();                    // Defino los pares de planetas con sus segundos

            // Uso indices de 0 a n - 1 para el digrafo (cada planeta a apunta a un planeta b en S segundos)
            grafo.get(planeta_a - 1).add(new Arista(planeta_b - 1, segundos));
        }

        List<List<Integer>> viajeros = new ArrayList<>(); // Lista de listas de viajeros que llegan en X tiempo al planeta n


        // Defino cada tiempo de "frenado" que tiene que hacer Martinez por los viajeros
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

    
    // Algoritmo de Dijkstra para encontrar el camino mínimo desde origen hasta destino
    static int dijkstra(List<List<Arista>> grafo, int origen, int destino, int tiempoInicial, List<List<Integer>> viajeros) {
        int n = grafo.size();
        int[] distancias = new int[n];                      // Creo un array que guarde las distancias entre planetas
        Arrays.fill(distancias, Integer.MAX_VALUE);         // Lleno el array distancias con el mayor valor posible (inf)
        
        PriorityQueue<Nodo> pq = new PriorityQueue<>();     
        // Uso PriorityQueue para poder correr Dijkstra:
        // Ordeno automaticamente los elementos segun mi compareTo del Nodo:
        // compare(this.distancia, otro.distancia)
        // Ordena los nodos por distancia ascendente (menor distancia = mayor prioridad)
        // Complejidad: O((V+E) log V) 

        distancias[origen] = tiempoInicial;                 // Comienzo el array con los segundos entre el planeta 1 y su adyacente
        pq.offer(new Nodo(origen, tiempoInicial));          // Inserta el planeta 1 con su tiempo en la cola de prioridad
        
        while (!pq.isEmpty()) {                             // Mientras tenga elementos por visitar:
            Nodo actual = pq.poll();                        // Obtengo el Nodo con la menor distancia acumulada
            int u = actual.id;                              // Obtengo el planeta
            int distActual = actual.distancia;              // Obtengo su distancia
            
            // Si ya fue procesado este nodo con una distancia mejor, lo ignoro
            if (distActual > distancias[u]) {
                continue;
            }
            
            // Si llegamos al destino, devuelvo la distancia
            if (u == destino) {
                return distancias[destino];
            }
            
            for (Arista arista : grafo.get(u)) {                // Itero sobre todos los vecinos del Nodo
                int v = arista.destino;                         // Obtengo un vecino 
                int peso = arista.peso;                         // Obtengo el peso (tiempo) del planeta vecino
                int nuevaDistancia = distancias[u] + peso;      // Sumo el tiempo obtenido a lo que ya tengo acumulado

                List<Integer> viajeros_v = viajeros.get(v);     // Obtengo la lista de tiempos en los que llegan los viajeros al planeta v
                
                for (int i = 0; i < viajeros_v.size(); i++){    // Evaluo los viajeros que llegan al mismo tiempo que nuevaDistancia
                    if (nuevaDistancia == viajeros_v.get(i)){
                        nuevaDistancia += 1;
                    }
                }
                
                if (nuevaDistancia < distancias[v]) {       // Si el nuevo camino es mas corto que el que tenemos guardado
                                                            // (En un principio siempre es True ya que iniciamos todo en +inf)
                    distancias[v] = nuevaDistancia;         // Lo guardo en la lista de distancias
                    pq.offer(new Nodo(v, nuevaDistancia));  // Agrego el vecino a la cola de prioridad con la distancia actualizada
                }
            }
        }
        
        // Si no se puede llegar al destino
        return -1;
    }
    
    static void viajeMinimo(List<List<Arista>> grafo, List<List<Integer>> viajeros){
        int n = grafo.size();
        int origen = 0;         // Planeta 1 (índice 0)
        int destino = n - 1;    // Planeta n (índice n-1)
        
        // Martínez comienza en el planeta 1 en el tiempo 0
        int tiempoInicial = 0;
        int resultado = dijkstra(grafo, origen, destino, tiempoInicial, viajeros);
        
        if (resultado == -1) {
            System.out.println(-1);
        } else {
            System.out.println(resultado);
        }
    }
}
