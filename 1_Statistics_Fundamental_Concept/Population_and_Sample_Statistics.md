Let $y_1,\ldots,y_N$ be the population values and $x_1,\ldots,x_n$ be the sample values.
| Aspect | Population parameter | Sample statistic / estimate |
|---|---|---|
| **Describes** | The entire group of interest | A sample from that group |
| **Availability** | Often unknown unless the entire population is observed | Calculated from observed sample data |
| **Variation** | Fixed for a defined population | Can change from sample to sample |
| **Size** | $N$: number of population observations | $n$: number of sample observations |
| **Mean** | $\mu=\dfrac{\sum_{j=1}^{N}y_j}{N}$ | $\bar{x}=\dfrac{\sum_{i=1}^{n}x_i}{n}$, estimates $\mu$ |
| **Variance** | $\sigma^2=\dfrac{\sum_{j=1}^{N}(y_j-\mu)^2}{N}$ | $s^2=\dfrac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}$, estimates $\sigma^2$ |
| **Standard deviation** | $\sigma=\sqrt{\dfrac{\sum_{j=1}^{N}(y_j-\mu)^2}{N}}$ | $s=\sqrt{\dfrac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}}$, estimates $\sigma$ |
| **Proportion** | $p=\dfrac{K}{N}$ | $\hat{p}=\dfrac{k}{n}$, estimates $p$ |
| **Minimum** | $y_{\min}=\min(y_1,\ldots,y_N)$ | $x_{\min}=\min(x_1,\ldots,x_n)$, estimates $y_{\min}$ |
| **Maximum** | $y_{\max}=\max(y_1,\ldots,y_N)$ | $x_{\max}=\max(x_1,\ldots,x_n)$, estimates $y_{\max}$ |
| **Quantile at level $\tau$** | $q_\tau=Q(\mathbf{y},\tau)$ | $\hat{q}_\tau=Q(\mathbf{x},\tau)$, estimates $q_\tau$ |
| **First quartile (25%)** | $Q_{1,\text{pop}}=Q(\mathbf{y},0.25)$ | $Q_{1,\text{sample}}=Q(\mathbf{x},0.25)$ |
| **Median (50%)** | $Q_{2,\text{pop}}=Q(\mathbf{y},0.50)$ | $Q_{2,\text{sample}}=Q(\mathbf{x},0.50)$ |
| **Third quartile (75%)** | $Q_{3,\text{pop}}=Q(\mathbf{y},0.75)$ | $Q_{3,\text{sample}}=Q(\mathbf{x},0.75)$ |