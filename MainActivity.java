package com.example.calculator;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    EditText n1, n2;
    TextView result;
    Button add, sub, mul, div;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        n1 = findViewById(R.id.n1);
        n2 = findViewById(R.id.n2);
        result = findViewById(R.id.result);
        add = findViewById(R.id.add);
        sub = findViewById(R.id.sub);
        mul = findViewById(R.id.mul);
        div = findViewById(R.id.div);

        add.setOnClickListener(v -> calculate('+'));
        sub.setOnClickListener(v -> calculate('-'));
        mul.setOnClickListener(v -> calculate('*'));
        div.setOnClickListener(v -> calculate('/'));
    }
    void calculate(char op) {
        String a = n1.getText().toString();
        String b = n2.getText().toString();
        if (a.isEmpty() || b.isEmpty()) {
            Toast.makeText(this, "Enter both numbers",
                    Toast.LENGTH_SHORT).show();
            return;
        }
        double x = Double.parseDouble(a);
        double y = Double.parseDouble(b);
        double ans = 0;
        switch (op) {
            case '+': ans = x + y; break;
            case '-': ans = x - y; break;
            case '*': ans = x * y; break;
            case '/':
                if (y == 0) {
                    result.setText("Cannot divide by zero");
                    return;
                }
                ans = x / y;
                break;
        }
        result.setText("Result: " + ans);
    }
}