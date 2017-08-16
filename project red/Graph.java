import java.util.Map;

/**
 * Created on 15/04/17 by dark magic.
 */
public class Graph implements CycleValidator, GraphData {
    private final Map<Index, NodeData> nodes;
    private final int row;
    private final int column;

    public Graph(Map<Index, NodeData> nodes, int row, int column) {
        this.nodes = nodes;

        resolveDependency();
        this.column = column;
        this.row = row;
    }

    private void resolveDependency() {
        for (Map.Entry<Index, NodeData> entry : nodes.entrySet()) {
            NodeData currentNode = entry.getValue();
            String[] expressions = currentNode.getExpression().split(" ");
            for (String unitExpression : expressions) {
                if (ExpressionUtils.doesExpressionContainAPosition(unitExpression)) {
                    Index index = ExpressionUtils.getPositionFromExpression(unitExpression);
                    currentNode.addNode(nodes.get(index));
                }
            }
        }
    }

    public boolean isCyclic() {
        boolean[][] visited = new boolean[row][column];
        boolean[][] recursiveStack = new boolean[row][column];

        for (Map.Entry<Index, NodeData> entry : nodes.entrySet()) {
            if (isCyclic(entry.getKey(), visited, recursiveStack)) {
                return true;
            }
        }
        return false;
    }

    public Map<Index, NodeData> getNodes() {
        return nodes;
    }

    private boolean isCyclic(Index key, boolean[][] visited, boolean[][] recursiveStack) {
        if (visited[key.getRolIndex()][key.getColIndex()] == false) {
            visited[key.getRolIndex()][key.getColIndex()] = true;
            recursiveStack[key.getRolIndex()][key.getColIndex()] = true;

            for (NodeData data : nodes.get(key).getParent()) {
                if (!visited[data.getIndex().getRolIndex()][data.getIndex().getColIndex()]
                        && isCyclic(data.getIndex(), visited, recursiveStack)) {
                    return true;
                } else if (recursiveStack[data.getIndex().getRolIndex()][data.getIndex().getColIndex()]) {
                    return true;
                }
            }
        }
        recursiveStack[key.getRolIndex()][key.getColIndex()] = false;
        return false;
    }
}
