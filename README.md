# Author : Nguinabe Josue

## Background

Principal Component Analysis (PCA) is a simple dimensionality reduction technique that can capture linear correlations between the features. For a given (standardized) data, PCA can be calculated by eigenvalue decomposition of covariance (or correlation) matrix of the data, or Singular Value Decomposition (SVD) of the data matrix. The data standardization includes mean removal and variance normalization.

## Data Set
In this Implementation, we use iris dataset. It consists of 50 samples from each of three species of Iris. The rows being the samples and the columns being: Sepal Length, Sepal Width, Petal Length and Petal Width.

### 1.   **Data standardization by using this following formula**

 Compute the mean as follows for each variables as
\begin{align*}
\text{Mean} &= \bar{X} = \frac{1}{n}\sum_{i=1}^{n} X_i \
\end{align*}
\begin{align*}
\text{Variance} &= \sigma^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X})^2
\end{align*}
Where $X_{i}$ represent the $i^{th}$ variable in the data set.
 To standardize a variable X using its mean ($\bar{X}$) and standard deviation ($\sigma$):

\begin{align*}
\text{Standardized }X &= \frac{X - \bar{X}}{\sigma}
\end{align*}

In this code, $\bar{X}$ represents the sample mean of the variable X, $\sigma$ represents the sample standard deviation of X, and X represents the original unstandardized variable. The resulting standardized variable has a mean of 0 and a standard deviation of 1.

### 2.   compute the covariance matrix

Determine the covariance matrix of the data set

$\text{Cov}(X_i,X_j) = \frac{1}{n-1}\sum_{k=1}^{n}(X_{i}^{k}-\bar{X}i)(X_{j}^{k}-\bar{X}_j)$
\begin{equation*}
\mathbf{S} = \frac{1}{n-1}\mathbf{X}^\top\mathbf{X},
\end{equation*}

where $\mathbf{X}$ is the $n \times p$ matrix of standardized data, and $\mathbf{S}$ is the $p \times p$ sample covariance matrix. The $(i,j)$th entry of $\mathbf{S}$ is given by

\begin{equation*}
s_{i,j} = \frac{1}{n-1}\sum_{k=1}^{n} x_{k,i}x_{k,j},
\end{equation*}

where $x_{k,i}$ and $x_{k,j}$ are the $i$th and $j$th standardized variables, respectively, for the $k$th observation.


It is important to note that the covariance matrix is a square, postive definate ,symmetric matric of dimension p by p where p is the number of variables.

### 3.   Compute the eigenvalue and eigenvector of our covariance matrix
Compute eigen values and standardised eigen vectors of the covariance matrix
Let $A$ be the covariance matrix of a dataset $X$, then the eigenvalue equation is given by:

\begin{equation*}
A\mathbf{v} = \lambda \mathbf{v}
\end{equation*}

where $\mathbf{v}$ is the eigenvector of $A$ and $\lambda$ is the corresponding eigenvalue.

To find the eigenvalues and eigenvectors, we can solve this equation using the characteristic polynomial of $A$:

\begin{equation*}
\det(A - \lambda I) = 0
\end{equation*}

where $I$ is the identity matrix of the same size as $A$. Solving for $\lambda$ gives the eigenvalues, and substituting each eigenvalue back into the equation $A\mathbf{v} = \lambda \mathbf{v}$ gives the corresponding eigenvectors.

######   Choose the number component that will the number of dimensions of the new feature subspace  

*   To be able to visualize our data on the new subspace we will choose 2  
*   Retain at least 95% percent from the cumulayive explained variance