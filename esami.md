# Svolgimento Esami Machine Learning

## File 09 - Esame 26_01_2022.pdf

---

### **Domanda 1**

**Domanda:** Supponiamo di voler creare un regressore lineare (Linear Regression) che permetta di stimare un valore \( y \) in base a due feature: \( x_1 \) e \( x_2 \). Supponiamo, inoltre, di avere i seguenti dati di training. Quanti parametri addestrabili ha il regressore descritto?

**Risposta:**  
Un regressore lineare con due feature (\( x_1 \) e \( x_2 \)) avrà 3 parametri addestrabili:  
- Un coefficiente per \( x_1 \) (\( \theta_1 \))  
- Un coefficiente per \( x_2 \) (\( \theta_2 \))  
- Un termine di bias (\( \theta_0 \))  

Quindi, il numero totale di parametri addestrabili è **3**.

---

### **Domanda 2**

**Domanda:** Supponiamo di aver addestrato una Logistic Regression su un dataset composto da due feature e di aver ottenuto i seguenti parametri:  
\( \theta_0 = [-5, 3] \); \( \theta_1 = [2, 3] \); \( \theta_2 = [3, 5] \).  
Calcolare la distanza del punto \( x = [0.6; 2.8]^T \) dal Decision Boundary individuato dal classificatore addestrato.

**Risposta:**  
La distanza di un punto \( x = [x_1, x_2]^T \) dal decision boundary di una Logistic Regression è data dalla formula:

\[
D(x, \text{Decision Boundary}) = \frac{|\theta_0 + \theta_1 x_1 + \theta_2 x_2|}{\sqrt{\theta_1^2 + \theta_2^2}}
\]

Sostituendo i valori dati:

\[
D(x, \text{Decision Boundary}) = \frac{|-5 + 2 \cdot 0.6 + 3 \cdot 2.8|}{\sqrt{2^2 + 3^2}} = \frac{|-5 + 1.2 + 8.4|}{\sqrt{4 + 9}} = \frac{|4.6|}{\sqrt{13}} \approx \frac{4.6}{3.605} \approx 1.28
\]

Quindi, la distanza è approssimativamente **1.28**.

---

### **Domanda 3**

**Domanda:** Utilizzare l'algoritmo di K-means per eseguire il clustering dei seguenti dati in due classi:  
_A = [5; 1]; B = [3; 1]; C = [3; 2]; D = [8; 1.5]; E = [7; 1]; F = [9; 2]_  
Valori iniziali dei centroidi: _C1 = [4; 1]; C2 = [9; 3]_.  
Selezionare i centroidi ottenuti a fine esecuzione.

**Risposta:**  
Dopo alcune iterazioni dell'algoritmo K-means, i centroidi convergono a:  
- _C1 = [3.5; 1.3]_  
- _C2 = [8; 1.5]_  

Quindi, la risposta corretta è:  
**b. _C1 = [3.5; 1.3]; C2 = [8; 1.5]_**

---

### **Domanda 4**

**Domanda:** Supponiamo di utilizzare una rete convolutiva per la classificazione di immagini 300x300 a colori (RGB - tre canali) rappresentata da:  
- Un layer convolutivo che ha 30 filtri con ognuno di dimensionalità 5x5.  
- Un maxpooling layer con stride=2 e dimensionalità 2x2.  
Di quanti parametri è composta la rete convolutiva (includendo anche i parametri di bias)?

**Risposta:**  
Il numero di parametri nel layer convolutivo è dato da:  
\[
\text{Numero di filtri} \times (\text{Dimensione del filtro} \times \text{Numero di canali} + 1 \text{ (bias)})
\]
Quindi:  
\[
30 \times (5 \times 5 \times 3 + 1) = 30 \times 76 = 2280
\]

Il maxpooling layer non ha parametri addestrabili. Quindi, il numero totale di parametri è **2280**.

---

### **Domanda 5**

**Domanda:** In quale dei seguenti problemi può essere utilizzata una rete ricorrente RNN One-to-Many?

**Risposta:**  
Una RNN One-to-Many è utilizzata in problemi in cui l'input è singolo e l'output è una sequenza. Un esempio è **Image Captioning**, dove l'input è un'immagine e l'output è una descrizione testuale.

Quindi, la risposta corretta è:  
**Image Captioning (data un'immagine il sistema restituisce una descrizione testuale)**

---

### **Domanda 6**

**Domanda:** Supponiamo di aver collezionato un piccolo dataset composto da informazioni derivanti da sei soluzioni. Per migliorare l’accuratezza del Classificatore SVM, decidiamo di effettuare una Min-Max Normalization dei dati. Calcolare il valore normalizzato della componente Sodio della soluzione 4 (prima riga del Test set).

**Risposta:**  
La Min-Max Normalization è data da:  
\[
x_{\text{norm}} = \frac{x - \text{min}}{\text{max} - \text{min}}
\]

Per il Sodio, i valori nel Train Set sono:  
- Minimo: 10.8  
- Massimo: 13.2  

Il valore di Sodio per la soluzione 4 è 12.2. Quindi:  
\[
x_{\text{norm}} = \frac{12.2 - 10.8}{13.2 - 10.8} = \frac{1.4}{2.4} \approx 0.58
\]

Quindi, il valore normalizzato è **0.58**.

---

## File 10 - Esame 10_02_2022.pdf

---

### **Domanda 1**

**Domanda:** Supponiamo di aver addestrato una Logistic Regression con la seguente ipotesi \( p(x) = g(\theta_0 + \theta_1 x_1 + \theta_2 x_2 + \theta_3 x_1^2 + \theta_4 x_2^2) \) (dove \( g \) è la Sigmoid function) su un dataset composto da due feature e di aver ottenuto i seguenti parametri:  
\( \theta_0 = -3; \theta_1 = 0; \theta_2 = 0; \theta_3 = 1; \theta_4 = 1 \).  
Calcolare la distanza del punto \( x = [0; 0]^T \) dal Decision Boundary individuato dal classificatore addestrato.

**Risposta:**  
Il decision boundary è dato da:  
\[
\theta_0 + \theta_1 x_1 + \theta_2 x_2 + \theta_3 x_1^2 + \theta_4 x_2^2 = 0
\]

Sostituendo i valori:  
\[
-3 + 0 \cdot 0 + 0 \cdot 0 + 1 \cdot 0^2 + 1 \cdot 0^2 = -3
\]

La distanza del punto \( x = [0; 0]^T \) dal decision boundary è:  
\[
D(x, \text{Decision Boundary}) = \frac{|-3|}{\sqrt{0^2 + 0^2 + 1^2 + 1^2}} = \frac{3}{\sqrt{2}} \approx 2.12
\]

Quindi, la distanza è approssimativamente **2.12**.

---

### **Domanda 2**

**Domanda:** Supponiamo di aver collezionato un piccolo dataset composto da informazioni derivanti da sei soluzioni. Per migliorare l’accuratezza del Classificatore SVM, decidiamo di effettuare una Mean Normalization dei dati. Calcolare il valore normalizzato della componente Sodio della soluzione 4 (prima riga del Test set).

**Risposta:**  
La Mean Normalization è data da:  
\[
x_{\text{norm}} = \frac{x - \text{mean}}{\text{max} - \text{min}}
\]

Per il Sodio, i valori nel Train Set sono:  
- Media: \( \frac{2.48 + 8.47 + 7.01}{3} \approx 5.99 \)  
- Minimo: 2.48  
- Massimo: 8.47  

Il valore di Sodio per la soluzione 4 è 2.8. Quindi:  
\[
x_{\text{norm}} = \frac{2.8 - 5.99}{8.47 - 2.48} = \frac{-3.19}{5.99} \approx -0.53
\]

Quindi, il valore normalizzato è **-0.53**.

---

### **Domanda 3**

**Domanda:** Se un modello addestrato di una rete neurale sembra essere in overfitting, quale delle seguenti strategie potrebbe essere interessante da applicare?

**Risposta:**  
Le strategie per ridurre l'overfitting sono:  
- **b. Usare Data Augmentation**  
- **c. Aumentare gli esempi di train**  
- **f. Applicare un fattore di regolarizzazione**  

Quindi, le risposte corrette sono **b, c, f**.

---

### **Domanda 4**

**Domanda:** Supponiamo di aver addestrato un classificatore che permetta di distinguere tra due classi attraverso l’analisi di due features: \( f_1 \) e \( f_2 \). Supponiamo, inoltre, di aver ottenuto le seguenti predizioni sul test set:

| Id | Actual Class | Prediction |
|----|--------------|------------|
| 1  | 1            | 1          |
| 2  | 1            | 0          |
| 3  | 1            | 1          |
| 4  | 1            | 1          |
| 5  | 0            | 0          |
| 6  | 0            | 0          |
| 7  | 0            | 1          |
| 8  | 0            | 1          |

Calcolare la F-score del classificatore.

**Risposta:**  
Per calcolare la F-score, dobbiamo prima calcolare Precision e Recall:  
- **True Positives (TP):** 3 (id 1, 3, 4)  
- **False Positives (FP):** 2 (id 7, 8)  
- **False Negatives (FN):** 1 (id 2)  

Precision = \( \frac{TP}{TP + FP} = \frac{3}{5} = 0.6 \)  
Recall = \( \frac{TP}{TP + FN} = \frac{3}{4} = 0.75 \)  

F-score = \( 2 \cdot \frac{Precision \cdot Recall}{Precision + Recall} = 2 \cdot \frac{0.6 \cdot 0.75}{0.6 + 0.75} = 2 \cdot \frac{0.45}{1.35} \approx 0.67 \)

Quindi, la F-score è **0.67**.

---

### **Domanda 5**

**Domanda:** Supponiamo di aver progettato la seguente rete neurale che riceva in input immagini RGB di dimensione 20x20:  
- Convolutional Layer con 5 filtri 3x3, opzione padding = “same”, funzione attivazione ReLU  
- Dense Layer con 10 unità  
- Un output layer (una unità) con funzione attivazione ReLU  
Quanti parametri ha la rete (includendo i bias)?

**Risposta:**  
1. **Convolutional Layer:**  
   - Numero di filtri: 5  
   - Dimensione di ogni filtro: 3x3x3 (3 canali RGB)  
   - Parametri: \( 5 \times (3 \times 3 \times 3 + 1) = 5 \times 28 = 140 \)  

2. **Dense Layer:**  
   - Input: 20x20x5 (output del convolutional layer)  
   - Parametri: \( 20 \times 20 \times 5 \times 10 + 10 = 20000 + 10 = 20010 \)  

3. **Output Layer:**  
   - Parametri: \( 10 \times 1 + 1 = 11 \)  

Totale parametri: \( 140 + 20010 + 11 = 20161 \)

Quindi, il numero totale di parametri è **20161**.

---

### **Domanda 6**

**Domanda:** Utilizzare l’algoritmo DBSCAN sui seguenti dati e determinare il numero di Border Point. I parametri dell’algoritmo sono: radius 1.9 e MinPts=3.

**Risposta:**  
Dopo aver applicato DBSCAN, il numero di Border Point è **2**.

---
