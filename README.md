"# matchLines_total" 
 This code takes two 2D arrays as inputs. Compares the two arrays by matching the
    values of the first column of the two arrays and outputs the values of the 
    second column of the second array and then combines that with the first 
    column of the second array. This is being specifically used to compare the
    wavelengths of the models and the observed data and then outputs the flux 
    values from the model that align with wavelengths that only occur in both 
    arrays. It then returns a 2D array containing the wavelengths present in 
    both arrays in the first column and the flux values present in both arrays
    in the second column. Any non-matching values are given a zero value and 
    then removed before the final 2D array is constructed. Output can be 
    chosen, either data flux or model flux. 1 for data and 0 for model.
