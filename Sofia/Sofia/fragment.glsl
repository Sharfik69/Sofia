precision highp float;
uniform float time;
uniform vec2 resolution;
varying vec3 fPosition;
varying vec3 fNormal;

void main()
{
  float l = (fNormal.x + fNormal.y + fNormal.z + 1.) / 3.;
  gl_FragColor = vec4(l, l, l, 1.0);
}