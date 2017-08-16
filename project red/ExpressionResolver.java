import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/**
 * Created on 15/04/17 by dark magic.
 */
public class ExpressionResolver {
    private final GraphData graph;
    private final Map<Index, Double> indexToValue = new HashMap<Index, Double>();

    public ExpressionResolver(GraphData graph) {
        this.graph = graph;
    }

    public void solveExpression() {
        for (Map.Entry<Index, NodeData> data : graph.getNodes().entrySet()) {
            if (!indexToValue.containsKey(data.getKey()))
                indexToValue.put(data.getKey(), solve(data.getValue()));
        }
    }

    public Map<Index, Double> getIndexToValues() {
        return this.indexToValue;
    }

    private Double solve(NodeData node) {
        Set<NodeData> parents = node.getParent();
        for (NodeData data : parents) {
            if (!indexToValue.containsKey(data.getIndex())) {
                solve(data);
            }
        }
        RPNSolver solver = new RPNSolver(node.getExpression(), indexToValue);
        double result = solver.solveIt();
        indexToValue.put(node.getIndex(), result);
        return result;
    }


}
