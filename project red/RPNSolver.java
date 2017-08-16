import java.util.Map;
import java.util.Stack;

/**
 * Created on 15/04/17 by dark magic.
 */
public class RPNSolver {
    private final String[] expression;
    private final Map<Index, Double> indexToValueMapping;

    public RPNSolver(String expression, Map<Index, Double> indexToValueMapping) {
        this.expression = expression.split(" ");
        this.indexToValueMapping = indexToValueMapping;
    }

    public double solveIt() {
        Stack<Object> values = new Stack<Object>();
        for (int i = 0; i < expression.length; i++) {
            if (BiOperator.isBiOperator(expression[i])) {
                Object latestValue = values.pop();
                Object olderValue = values.pop();
                Double result = getResult(latestValue, olderValue, expression[i]);
                values.push(result);
            } else {
                values.add(expression[i]);
            }
        }
        if (values.peek() instanceof String) {
            return convertValueToDouble(values.pop());
        } else {
            return (Double) values.pop();
        }
    }

    private Double getResult(Object latestValue, Object olderValue, String expression) {
        Double operand2 = convertValueToDouble(latestValue);
        Double operand1 = convertValueToDouble(olderValue);
        BiOperator operator = BiOperator.getBiOperator(expression);
        return operator.getValue(operand1, operand2);
    }

    private Double convertValueToDouble(Object latestValue) {
        if (ExpressionUtils.doesExpressionContainAPosition(String.valueOf(latestValue))) {
            Index position = ExpressionUtils.getPositionFromExpression(String.valueOf(latestValue));
            Double valueForPosition = indexToValueMapping.get(position);
            if (UniOperator.doesExpressionContainUniOperator(String.valueOf(latestValue))) {
                UniOperator operator = UniOperator.getUniOperator(String.valueOf(latestValue));
                return operator.getValue(valueForPosition);
            }
            return valueForPosition;
        }

        if (latestValue instanceof Double) {
            return (Double) latestValue;
        } else if (latestValue instanceof String) {
            return 1.0 * Integer.parseInt(String.valueOf(latestValue));
        }

        throw new RuntimeException("UnKnown expression!!");
    }
}
