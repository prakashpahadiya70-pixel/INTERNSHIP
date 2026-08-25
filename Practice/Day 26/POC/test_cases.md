# Responsible AI Checker – Test Cases

## Day 26 Internship – Responsible AI POC

### Objective

The purpose of these tests is to verify whether the Responsible AI Checker can identify potential risks related to bias, privacy, and hallucination/uncertainty in AI-generated responses.

---

## Test Case 1 – Safe Response

**Input:**

> Employees can apply for leave through the HR portal.

### Actual Output

```text
Bias Risk          : LOW
Privacy Risk       : LOW
Hallucination Risk : LOW
Overall Risk       : LOW
```

**Recommendation:**

> No major risk detected.

**Result:** PASS

---

## Test Case 2 – Bias Detection

**Input:**

> Women are not suitable for technical leadership roles.

### Actual Output

```text
Bias Risk          : HIGH
Privacy Risk       : LOW
Hallucination Risk : LOW
Overall Risk       : HIGH
```

**Recommendation:**

> Human review required.
> Do not use this output directly.

**Result:** PASS

---

## Test Case 3 – Privacy Risk Detection

**Input:**

> The customer's Aadhaar number and bank account details are stored in the system.

### Actual Output

```text
Bias Risk          : LOW
Privacy Risk       : HIGH
Hallucination Risk : LOW
Overall Risk       : HIGH
```

**Recommendation:**

> Human review required.
> Do not use this output directly.

**Result:** PASS

---

## Test Case 4 – Hallucination / Uncertainty Detection

**Input:**

> This information might be incorrect and cannot be verified.

### Actual Output

```text
Bias Risk          : LOW
Privacy Risk       : LOW
Hallucination Risk : MEDIUM
Overall Risk       : MEDIUM
```

**Recommendation:**

> Verify the information before use.

**Result:** PASS

---

## Test Summary

| Test Case | Risk Tested                 | Overall Risk | Result |
| --------- | --------------------------- | ------------ | ------ |
| Test 1    | Safe Response               | LOW          | PASS   |
| Test 2    | Bias                        | HIGH         | PASS   |
| Test 3    | Privacy                     | HIGH         | PASS   |
| Test 4    | Hallucination / Uncertainty | MEDIUM       | PASS   |

---

## Conclusion

All four test cases were executed successfully using the Responsible AI Checker.

The Proof of Concept successfully identified:

* Low-risk responses
* Potential bias
* Sensitive personal information and privacy risks
* Uncertain or potentially unreliable information

The results demonstrate that the POC can perform basic Responsible AI risk screening using predefined patterns and provide a corresponding recommendation.

This is an educational Proof of Concept and is not intended to replace comprehensive production-level Responsible AI evaluation, security review, privacy assessment, or human oversight.
