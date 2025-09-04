#include <stdio.h>

// arm-linux-gnueabihf-gcc -mfloat-abi=hard -mfpu=vfp -o test_simple test.c

float calc_lowpass_alpha_dt(float dt, float cutoff_freq)
{

  if (dt <= 0.0)  {
      return 0.0; // Invalid input
  }

  if (cutoff_freq <= 0.0) {
    return 1.0;
  }

  float rc = 10 / (0.6283185 * cutoff_freq);
  float ret_val = dt / (dt + rc);
  return ret_val;
}

int main(int argc, char** argv) {
  float a = calc_lowpass_alpha_dt(5.0, 6.0);
  printf("%f\n", a);
  return a;
}

