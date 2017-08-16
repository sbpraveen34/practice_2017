/**
 * Created on 15/04/17 by dark magic.
 */
public class ExpressionUtils {
    private static Index getIndexFor(String expression) {
        int row = expression.charAt(0) - 'A';

        if (!(row >= 0 && row <= 25)) throw new RuntimeException("Wrong row count");

        int column = Integer.parseInt(expression.substring(1)) - 1;
        return new Index(row, column);
    }

    public static boolean doesExpressionContainAPosition(String expression) {
        try {
            getPositionFromExpression(expression);
            return true;
        } catch (Exception ex) {
            // do nothing
        }

        return false;
    }

    public static Index getPositionFromExpression(String expression) {
        if (expression.endsWith(UniOperator.POSTADD.getOperator())) {
            return getIndexFor(expression.substring(0, expression.length() - UniOperator.POSTADD.getOperator().length()));
        } else if (expression.startsWith(UniOperator.PREADD.getOperator())) {
            return getIndexFor(expression.substring(UniOperator.PREADD.getOperator().length(), expression.length()));
        } else if (expression.startsWith(UniOperator.PRESUBTRACT.getOperator())) {
            return getIndexFor(expression.substring(UniOperator.PRESUBTRACT.getOperator().length(), expression.length()));
        } else if (expression.endsWith(UniOperator.POSTSUBTRACT.getOperator())) {
            return getIndexFor(expression.substring(0, expression.length() - UniOperator.POSTSUBTRACT.getOperator().length()));
        } else if (expression.startsWith(UniOperator.SUBTRACT.getOperator())) {
            return getIndexFor(expression.substring(UniOperator.SUBTRACT.getOperator().length(), expression.length()));
        }
        return getIndexFor(expression);
    }
}
