import java.util.HashSet;
import java.util.Set;

/**
 * Created on 15/04/17 by dark magic.
 */
public class NodeData {
    private final String expression;
    private final Index index;
    private Set<NodeData> parent;

    public NodeData(String expression, Index index) {
        this.expression = expression;
        this.index = index;
        this.parent = new HashSet<NodeData>();
    }

    public String getExpression() {
        return expression;
    }

    public Index getIndex() {
        return this.index;
    }

    public Set<NodeData> getParent() {
        return parent;
    }

    public void addNode(NodeData node) {
        this.parent.add(node);
    }
}
