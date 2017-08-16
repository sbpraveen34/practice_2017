import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Created on 15/04/17 by dark magic.
 */
public class GraphFactory {
    public static Graph createGraph(List<String> expressions, int row, int col) {
        Map<Index, NodeData> mapp = new HashMap<Index, NodeData>();
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                Index index = new Index(i, j);
                String expression = expressions.get(j + col * (i));
                NodeData nodeData = new NodeData(expression, index);
                mapp.put(index, nodeData);
            }
        }

        return new Graph(mapp, row, col);
    }
}
