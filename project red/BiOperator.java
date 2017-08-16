/**
 * Created on 15/04/17 by dark magic.
 */
public enum BiOperator {
    ADD {
        public double getValue(double operand1, double operand2) {
            return operand1 + operand2;
        }

        public char getOperator() {
            return '+';
        }
    },
    SUBTRACT {
        public double getValue(double operand1, double operand2) {
            return operand1 - operand2;
        }

        public char getOperator() {
            return '-';
        }
    },
    MULTIPLE {
        public double getValue(double operand1, double operand2) {
            return operand1 * operand2;
        }

        public char getOperator() {
            return '*';
        }
    },
    DIVIDE {
        public double getValue(double operand1, double operand2) {
            return operand1 / operand2;
        }

        public char getOperator() {
            return '/';
        }
    };

    public abstract double getValue(double operand1, double operand2);

    public abstract char getOperator();

    public static BiOperator getBiOperator(String expression) {
        if (expression.equalsIgnoreCase(String.valueOf(ADD.getOperator()))) return ADD;
        if (expression.equalsIgnoreCase(String.valueOf(SUBTRACT.getOperator()))) return SUBTRACT;
        if (expression.equalsIgnoreCase(String.valueOf(MULTIPLE.getOperator()))) return MULTIPLE;
        if (expression.equalsIgnoreCase(String.valueOf(DIVIDE.getOperator()))) return DIVIDE;
        throw new RuntimeException("No bioperator exist");
    }

    public static boolean isBiOperator(String expresion) {
        boolean isBiOperator = false;
        try {
            BiOperator operator = getBiOperator(expresion);
            return true;
        } catch (Exception ex) {
            // do nothing
        }
        return false;
    }
}
