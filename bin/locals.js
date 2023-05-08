// --------------------------------------------------------
function getJacobian(node1, node2, node3) {
  return (
    (node2.x - node1.x) * (node3.y - node1.y) -
    (node3.x - node1.x) * (node2.y - node1.y)
  );
}
// --------------------------------------------------------
function getOneA(node1, node2, node3) {
  return [
    [node3.y - node1.y, node1.x - node3.x],
    [node1.y - node2.y, node2.x - node1.x],
  ];
}
// --------------------------------------------------------
function getArea(jacobian) {
  return jacobian / 2;
}
// --------------------------------------------------------
export function getLocalB(Q, node1, node2, node3) {
  const jacobian = getJacobian(node1, node2, node3);
  const product = (Q * jacobian) / 6;
  const aux_matrix = [[1], [1], [1]];
  let localB = multiplyConstantByMatrix(product,aux_matrix);
  
  return formatMatrix(localB);
}
// --------------------------------------------------------
export function getLocalK(K, node1, node2, node3) {
  let localK = 0;

  const jacobian = getJacobian(node1, node2, node3);

  const product = (K * getArea(jacobian)) / (jacobian * jacobian);

  localK = multiplyConstantByMatrix(
    product,
    matrixProduct(node1, node2, node3)
  );

  return formatMatrix(localK);
}
// --------------------------------------------------------
function transposeMatrix(M) {
  const rows = M.length;
  const cols = M[0].length;

  // Create a new matrix to store the transposed values
  const result = new Array(cols);
  for (let i = 0; i < cols; i++) {
    result[i] = new Array(rows);
  }

  // Populate the transposed matrix
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      result[j][i] = M[i][j];
    }
  }

  return result;
}

// --------------------------------------------------------
export function multiplyConstantByMatrix(k, M) {
  const result = [];

  // Multiply each element in the matrix by the constant
  for (let i = 0; i < M.length; i++) {
    const row = [];
    for (let j = 0; j < M[i].length; j++) {
      row.push(k * M[i][j]);
    }
    result.push(row);
  }

  return result;
}
// --------------------------------------------------------
function matrixProduct(node1, node2, node3) {
  const A = getOneA(node1, node2, node3);
  const B = [
    [-1, 1, 0],
    [-1, 0, 1],
  ];
  const AT = transposeMatrix(A);
  const BT = transposeMatrix(B);

  const BTAT = multiplyMatrices(BT, AT);
  const BTATA = multiplyMatrices(BTAT, A);
  const result = multiplyMatrices(BTATA, B);
  return result;
}
// ---------------------------------------------------------
function multiplyMatrices(m1, m2) {
  const result = [];

  for (let i = 0; i < m1.length; i++) {
    result[i] = [];
    for (let j = 0; j < m2[0].length; j++) {
      let sum = 0;
      for (let k = 0; k < m1[0].length; k++) sum += m1[i][k] * m2[k][j];
      result[i][j] = sum;
    }
  }

  return result;
}
// -----------------------------------------------------------
function formatMatrix(matrix) {
  const formattedMatrix = [];
  for (let i = 0; i < matrix.length; i++) {
    formattedMatrix[i] = [];
    for (let j = 0; j < matrix[i].length; j++) {
      const formattedNumber = matrix[i][j].toFixed(2);
      formattedMatrix[i][j] = formattedNumber;
    }
  }
  return formattedMatrix;
}
