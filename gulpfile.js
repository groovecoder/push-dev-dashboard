'use strict';

var gulp = require('gulp');
var jshint = require('gulp-jshint');

gulp.task('test', ['test:jshint']);

gulp.task('test:jshint', function() {
    return gulp.src(['**/*.js', '!staticfiles/**/*.js', '!node_modules/**/*.js', '!env/**/*.js'])
               .pipe(jshint())
               .pipe(jshint.reporter('default'));
});
