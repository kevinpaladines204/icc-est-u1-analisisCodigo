import java.util.Random;

public class Benchmarking {


    private MetodosOrdenamiento mOrdenamiento;

    public Benchmarking(){
        long currentMillis = System.currentTimeMillis();
        long currentNano= System.nanoTime();

        System.out.println("Millis :" + currentMillis);
        System.out.println("Nano :" + currentNano);

        mOrdenamiento= new MetodosOrdenamiento();
        int [] arreglo= generarArregloAleatorio(1_000_000_000);
        Runnable tarea= ()-> mOrdenamiento.burbujaTradicional(arreglo);

        double tiempoDuracionMillis= medirConCurrentTimeMilles(tarea);
        double tiempoDuracionNano= medirConNanoTime(tarea);
        System.out.println("Tiempo en milisegundos :" + tiempoDuracionMillis);
        System.out.println("Tiempo en nanosegundos :" + tiempoDuracionNano);
    }

    public int[]generarArregloAleatorio(int tamano){
        //crear un arreglo aleatorio desde 0 al 99.999
        int []array = new int[tamano];
        Random random = new Random();
        for(int i=0;i<tamano; i++){
            array[i]= random.nextInt(10000);
        }
        return array;
    }

    public double medirConCurrentTimeMilles(Runnable tarea){
        long inicio= System.currentTimeMillis();
        tarea.run();
        long fin =System.currentTimeMillis();
        double tiempoSegundos =(fin - inicio)/ 1000.0 ;
        return tiempoSegundos;
    }

    public double medirConNanoTime(Runnable tarea){
        long inicio =System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin -inicio)/1_000_000_000.0;
    }
}
