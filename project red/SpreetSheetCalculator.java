import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Created on 15/04/17 by dark magic.
 */
public class SpreetSheetCalculator {
    private final int row;
    private final int column;
    private final List<String> expression;
    private Graph graph;

    public SpreetSheetCalculator(int row, int column, List<String> expression) {
        this.row = row;
        this.column = column;
        this.expression = expression;
    }

    public Map<Index, Double> exec() {
        CycleValidator graph = GraphFactory.createGraph(expression, row, column);
        if (graph.isCyclic()) {
            System.out.println("Sorry your graph is cyclic!!");
            System.exit(1);
        }
        ExpressionResolver expressionResolver = new ExpressionResolver((GraphData) graph);
        expressionResolver.solveExpression();
        return expressionResolver.getIndexToValues();
    }

    public static void main(String[] args) {
        //System.out.println(args.length);
        int column = Integer.parseInt(args[0].split(" ")[0]);
        int row = Integer.parseInt(args[0].split(" ")[1]);
//        int column = 3;
//        int row = 2;
        List<String> expression = new ArrayList<String>();
//        expression.add("A2");
//        expression.add("4 5 *");
//        expression.add("A1");
//        expression.add("A1++ --B2 / 2 +");
//        expression.add("3");
//        expression.add("39 B1 B2 * /");
//        expression.add("A2");
//        expression.add("A1");
        for (int i = 1; i < args.length; i++) {
            expression.add(args[i]);
        }

        SpreetSheetCalculator calculator = new SpreetSheetCalculator(row, column, expression);
        Map<Index, Double> values = calculator.exec();
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                System.out.println(String.format("%.5f", values.get(new Index(i, j))));
            }
        }
    }
}
