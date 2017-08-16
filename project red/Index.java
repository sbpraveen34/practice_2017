/**
 * Created on 15/04/17 by dark magic.
 */
public class Index {
    private final int rolIndex;
    private final int colIndex;

    public Index(int rolIndex, int colIndex) {
        this.rolIndex = rolIndex;
        this.colIndex = colIndex;
    }

    public int getRolIndex() {
        return rolIndex;
    }

    public int getColIndex() {
        return colIndex;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Index index = (Index) o;

        if (rolIndex != index.rolIndex) return false;
        return colIndex == index.colIndex;

    }

    @Override
    public int hashCode() {
        int result = rolIndex;
        result = 31 * result + colIndex;
        return result;
    }
}
