/**
 * Created on 15/04/17 by dark magic.
 */
public enum UniOperator {
    POSTADD {
        public double getValue(double val) {
            return val;
        }

        public String getOperator() {
            return "++";
        }
    },
    PREADD {
        public double getValue(double val) {
            return ++val;
        }

        public String getOperator() {
            return "++";
        }

    },
    POSTSUBTRACT {
        public double getValue(double val) {
            return val--;
        }

        public String getOperator() {
            return "--";
        }

    },
    PRESUBTRACT {
        public double getValue(double val) {
            return --val;
        }

        public String getOperator() {
            return "--";
        }
    },
    SUBTRACT {
        public double getValue(double val) {
            return -val;
        }

        public String getOperator() {
            return "-";
        }
    };

    public abstract double getValue(double val);

    public abstract String getOperator();

    public static UniOperator getUniOperator(String expression) {
        if (expression.endsWith(UniOperator.POSTADD.getOperator())) {
            return POSTADD;
        } else if (expression.startsWith(UniOperator.PREADD.getOperator())) {
            return PREADD;
        } else if (expression.startsWith(UniOperator.PRESUBTRACT.getOperator())) {
            return PRESUBTRACT;
        } else if (expression.endsWith(UniOperator.POSTSUBTRACT.getOperator())) {
            return POSTSUBTRACT;
        } else if (expression.startsWith(UniOperator.SUBTRACT.getOperator())) {
            return SUBTRACT;
        }
        throw new RuntimeException("No Uni Expression!");
    }

    public static boolean doesExpressionContainUniOperator(String expression) {
        try {
            getUniOperator(expression);
            return true;
        } catch (Exception ex) {
            // do nothing
        }
        return false;
    }


}